
<script lang="ts">
	import { user, authLoading } from "$lib/stores/auth";
	import type { ValidationResponse } from "$lib/api/submit";
	import {
	validateMapping,
	submitMapping,
	} from "$lib/api/submit";
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'layout-dashboard':
			'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
		'file-down':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
		settings:
			'<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
		check: '<path d="M20 6 9 17l-5-5"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
		library: '<path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/>',
		'search-check':
			'<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		'shield-check':
			'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
		upload:
			'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>',
		'rotate-ccw':
			'<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/>',
		'arrow-down': '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>'
	};
	
	function getInitials(name: string) {
    return name
        .split(" ")
        .map((part) => part[0])
        .join("")
        .slice(0, 2)
        .toUpperCase();
	}

	// Form state
	let md5 = $state('');
	let olid = $state('');
	let submitting = $state(false);


	// Mock validation result — pure frontend, assume validation completed.
	type BookRecord = {
    	title: string;
    	authors: string[];
    	publishers: string[];
    	publish_date: string | null;
    	languages: string[];
	};


	const recordFields = [
    	{ key: "title", label: "Title" },
    	{ key: "authors", label: "Authors" },
    	{ key: "publishers", label: "Publisher" },
    	{ key: "publish_date", label: "Published" },
    	{ key: "languages", label: "Language" }
	] as const;

	let md5Record = $state<BookRecord | null>(null);
let openLibraryRecord = $state<BookRecord | null>(null);

let validationChecks = $state<string[]>([]);
let validationResult = $state<ValidationResponse | null>(null);

let confidence = $state(0);
let validated = $state(false);
let loading = $state(false);


	async function handleValidate(event: SubmitEvent) {
    event.preventDefault();

    console.log("Validate clicked");
	console.log("md5 =", md5);
    console.log("olid =", olid);

    loading = true;

    try {
        const result = await validateMapping(md5, olid);

        console.log(result);
		

        md5Record = result.anna_record;
        openLibraryRecord = result.openlibrary_record;

        confidence = result.confidence;
        validationChecks = result.reasons;
        validationResult = result;

        validated = true;

        console.log("validated =", validated);

    } catch (err) {
        console.error(err);
    } finally {
        loading = false;
    }
}
	async function handleSubmit() {
    if (!validationResult) return;

    submitting = true;

    try {
        const result = await submitMapping({
            md5,
            olid,
            anna_record: validationResult.anna_record,
            openlibrary_record: validationResult.openlibrary_record,
            confidence: validationResult.confidence,
            match: validationResult.match,
        });

        console.log(result);

        alert("Mapping submitted successfully!");

        reset();

    } catch (err) {
        console.error(err);
        alert("Submission failed.");
    } finally {
        submitting = false;
    }
}

	function reset(): void {
		md5 = '';
		olid = '';

		validated = false;
    	confidence = 0;

    	md5Record = null;
    	openLibraryRecord = null;
		validationResult = null;
    	validationChecks = [];
	}
	function clearValidation() {
    validated = false;
    validationResult = null;
    confidence = 0;
    md5Record = null;
    openLibraryRecord = null;
    validationChecks = [];
	}

	const guidelines: string[] = [
		'Every submission is reviewed by a human moderator.',
		'Automatic validation assists moderators but never replaces human review.',
		'Approved mappings become part of Mond’s permanent public dataset.'
	];
</script>

{#snippet icon(name: string, size: number = 16, strokeWidth: number = 1.5)}
	<svg
		xmlns="http://www.w3.org/2000/svg"
		width={size}
		height={size}
		viewBox="0 0 24 24"
		fill="none"
		stroke="currentColor"
		stroke-width={strokeWidth}
		stroke-linecap="round"
		stroke-linejoin="round"
		aria-hidden="true"
	>
		{@html iconPaths[name]}
	</svg>
{/snippet}

	{#snippet recordColumn(
    label: string,
    iconName: string,
    tag: string,
    record: BookRecord | null
)}

{#if record}

<div>
    <div class="mb-5 flex items-center justify-between">
        <span class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
            {@render icon(iconName,13)}
            {label}
        </span>

        <span class="mono text-[11px] text-[#A1A1AA]">
            {tag}
        </span>
    </div>

    <dl class="space-y-3">

        {#each recordFields as field}

            <div class="flex items-baseline justify-between gap-4 border-b border-[#F4F4F5] pb-3 last:border-0">

                <dt class="text-xs text-[#A1A1AA]">
                    {field.label}
                </dt>

                <dd class="text-right text-sm text-[#3F3F46]">

                    {#if Array.isArray(record[field.key])}

                        {record[field.key].length
                            ? record[field.key].join(", ")
                            : "-"}

                    {:else}

                        {record[field.key] ?? "-"}

                    {/if}

                </dd>

            </div>

        {/each}

    </dl>

</div>

{:else}

<p>No record.</p>

{/if}

{/snippet}

<svelte:head>
	<title>Submit a mapping — Mond</title>
	<meta
		name="description"
		content="Link an MD5 record to an Open Library edition. Mond validates metadata automatically before human review."
	/>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&family=Newsreader:ital,wght@1,300&family=JetBrains+Mono:wght@300;400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="page min-h-screen bg-[#FAFAFA] text-[#18181B] antialiased">
	<!-- ============ NAV ============ -->
	<header class="border-b border-[#E4E4E7] bg-white/80 backdrop-blur-sm">
		<nav class="mx-auto flex max-w-6xl items-center justify-between px-6 py-4">
			<div class="flex items-center gap-8">
				<a href="/" class="group flex items-center gap-3">
					<span class="crescent-sm" aria-hidden="true"></span>
					<span class="text-[15px] font-normal tracking-[0.22em] uppercase text-[#18181B]">
						Mond
					</span>
				</a>

				<div class="hidden items-center gap-1 sm:flex">
					<a
						href="/dashboard"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
					>
						{@render icon('layout-dashboard', 15)}
						Dashboard
					</a>
					
					<a
						href="/settings"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
					>
						{@render icon('settings', 15)}
						Settings
					</a>
				</div>
			</div>

			<!-- User menu: native <details> for keyboard & no-JS accessibility -->
			<details class="user-menu relative">
				<summary
					class="flex cursor-pointer list-none items-center gap-2.5 rounded-md px-2 py-1.5 transition-colors hover:bg-[#F4F4F5]"
					aria-label="Account menu for {$user?.username}"
				>
					<span
						class="flex h-8 w-8 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] text-xs font-medium text-[#6D28D9]"
					>
						{$user ? getInitials($user.username) : ""}
					</span>
					<span class="hidden text-sm font-light text-[#3F3F46] sm:inline">{$user?.username}</span>
					<span class="text-[#A1A1AA]">{@render icon('chevron-down', 14)}</span>
				</summary>

				<div
					class="paper absolute right-0 z-30 mt-2 w-56 overflow-hidden rounded-lg py-1.5"
					role="menu"
				>
					<div class="border-b border-[#F4F4F5] px-4 py-3">
						<p class="text-sm text-[#18181B]">{$user?.username}</p>
						<p class="mono mt-0.5 text-xs text-[#A1A1AA]">{$user?.email}</p>
					</div>
					<a
						href="/settings"
						role="menuitem"
						class="flex items-center gap-2.5 px-4 py-2.5 text-sm font-light text-[#3F3F46] transition-colors hover:bg-[#F4F4F5]"
					>
						{@render icon('user', 14)}
						Profile & settings
					</a>
					<a
						href="/logout"
						role="menuitem"
						class="flex items-center gap-2.5 px-4 py-2.5 text-sm font-light text-[#3F3F46] transition-colors hover:bg-[#F4F4F5]"
					>
						{@render icon('log-out', 14)}
						Sign out
					</a>
				</div>
			</details>
		</nav>

		<!-- Mobile nav row -->
		<div class="flex items-center gap-1 border-t border-[#F4F4F5] px-6 py-2 sm:hidden">
			<a
				href="/dashboard"
				class="flex items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('layout-dashboard', 14)}
				Dashboard
			</a>
			<a
				href="/dataset"
				class="flex items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('file-down', 14)}
				Dataset
			</a>
			<a
				href="/settings"
				class="flex items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('settings', 14)}
				Settings
			</a>
		</div>
	</header>

	<main class="morning">
		<div class="mx-auto max-w-2xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ HERO ============ -->
			<section aria-labelledby="submit-heading" class="text-center">
				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Contributor workflow
				</p>
				<h1
					id="submit-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Submit a new mapping.
				</h1>
				<p class="mx-auto mt-4 max-w-md text-sm font-light leading-relaxed text-[#52525B]">
					Link an MD5 record to an Open Library edition. Mond
					automatically validates metadata before the submission is reviewed by
					a human moderator.
				</p>
			</section>

			<!-- ============ SUBMISSION FORM ============ -->
			<section aria-labelledby="form-heading" class="mt-14">
				<h2 id="form-heading" class="sr-only">Mapping details</h2>

				<form class="paper rounded-lg p-6 sm:p-8" onsubmit={handleValidate}>
					<div class="mb-6 flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
						{@render icon('book-marked', 13)}
						Mapping details
					</div>

					<div class="space-y-7">
						<div>
							<label for="md5" class="block text-sm font-light text-[#3F3F46]">
								MD5
							</label>
							<input
								id="md5"
								name="md5"
								type="text"
								bind:value={md5}
								oninput={clearValidation}
								placeholder="8efbf8e9f8b4592c7b0dbedec9c0ec05"
								autocomplete="off"
								spellcheck="false"
								aria-describedby="md5-help"
								class="mono mt-2 w-full rounded-md border border-[#E4E4E7] bg-white px-4 py-3 text-sm text-[#18181B] shadow-sm transition-colors placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/50 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
							/>
							<p id="md5-help" class="mt-2 text-xs font-light text-[#A1A1AA]">
								32-character MD5 hash
							</p>
						</div>

						<div>
							<label for="olid" class="block text-sm font-light text-[#3F3F46]">
								Open Library Edition
							</label>
							<input
								id="olid"
								name="olid"
								type="text"
								bind:value={olid}
								placeholder="OL7602281M"
								oninput={clearValidation}
								autocomplete="off"
								spellcheck="false"
								aria-describedby="olid-help"
								class="mono mt-2 w-full rounded-md border border-[#E4E4E7] bg-white px-4 py-3 text-sm text-[#18181B] shadow-sm transition-colors placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/50 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
							/>
							<p id="olid-help" class="mt-2 text-xs font-light text-[#A1A1AA]">
								Edition identifier beginning with OL
							</p>
						</div>
					</div>

					<div class="mt-8 border-t border-[#F4F4F5] pt-6">
						<button
							type="submit"
							disabled={loading || !md5.trim() || !olid.trim()}
							class="flex w-full items-center justify-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3.5 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
						>
							{#if loading}
    							Validating...
							{:else}
    							{@render icon('search-check',15)}
    								Validate mapping
							{/if}
						</button>
					</div>
				</form>
			</section>

			<!-- Connector between form and result -->
			{#if validated}
				<div class="connector" aria-hidden="true">
					<span class="connector-node">{@render icon('arrow-down', 11)}</span>
				</div>
			{/if}

			<!-- ============ VALIDATION RESULT ============ -->
			{#if validated}
			<section aria-labelledby="result-heading">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-8 flex items-center justify-between">
						<h2
							id="result-heading"
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							{@render icon('search-check', 13)}
							Validation result
						</h2>
						<span class="rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 px-2.5 py-0.5 text-[11px] text-[#16A34A]">
							Completed
						</span>
					</div>

					<!-- Source & target records -->
					<div class="grid gap-10 sm:grid-cols-2 sm:gap-8">
						{@render recordColumn("MD5", 'book-marked', 'source', md5Record)}
						{@render recordColumn('Open Library', 'library', 'target', openLibraryRecord)}
					</div>

					<!-- Automated checks -->
					<div class="mt-10 border-t border-[#F4F4F5] pt-8">
						<h3 class="mb-5 flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
							{@render icon('shield-check', 13)}
							Automated validation
						</h3>
						<ul class="space-y-3">
							{#each validationChecks as check}
								<li class="flex items-center gap-3 text-sm font-light text-[#3F3F46]">
									<span class="flex h-4 w-4 items-center justify-center rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]">
										{@render icon('check', 9, 2.5)}
									</span>
									{check}
								</li>
							{/each}
						</ul>
					</div>

					<!-- Confidence -->
					<div class="mt-10 rounded-lg border border-[#8B5CF6]/20 bg-[#8B5CF6]/[0.04] px-6 py-8 text-center">
						<p class="mono text-4xl font-light text-[#6366F1] sm:text-5xl">
							{confidence}<span class="text-2xl sm:text-3xl">%</span>
						</p>
						<p class="mt-2 text-xs font-light tracking-wide text-[#71717A]">
							{#if confidence >= 90}
        						Excellent match
    						{:else if confidence >= 70}
        						Good match
    						{:else if confidence >= 45}
        						Possible match
    						{:else}
        						Poor match
    						{/if}
						</p>
						<div
							class="mx-auto mt-5 h-1 w-full max-w-xs overflow-hidden rounded-full bg-[#8B5CF6]/10"
							role="meter"
							aria-valuenow={confidence}
							aria-valuemin="0"
							aria-valuemax="100"
							aria-label="Validation confidence"
						>
							<div
								class="h-full rounded-full bg-[#6366F1] transition-[width] duration-700"
								style="width: {confidence}%"
							></div>
						</div>
					</div>

					<!-- Actions -->
					<div class="mt-8 flex flex-col gap-3 border-t border-[#F4F4F5] pt-6 sm:flex-row">
						<button
							type="button"
							onclick={handleSubmit}
    						disabled={submitting || !validationResult}
							class="flex flex-1 items-center justify-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3.5 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
						>
							{#if submitting}
    Submitting...
{:else}
    {@render icon('upload',15)}
    Submit mapping
{/if}
						</button>
						<button
							type="button"
							onclick={reset}
							class="flex items-center justify-center gap-2.5 rounded-md border border-[#E4E4E7] bg-white px-6 py-3.5 text-sm text-[#71717A] shadow-sm transition-colors hover:border-[#D4D4D8] hover:text-[#18181B]"
						>
							{@render icon('rotate-ccw', 14)}
							Reset
						</button>
					</div>

					<p class="mt-5 text-center text-xs font-light text-[#A1A1AA]">
						Your submission will be placed in the review queue and read by a moderator.
					</p>
				</div>
			</section>
			{/if}


			<!-- ============ BEFORE YOU SUBMIT ============ -->
			<section aria-labelledby="guidelines-heading" class="mt-10">
				<div class="paper rounded-lg p-6 sm:p-8">
					<h2
						id="guidelines-heading"
						class="mb-5 flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
					>
						{@render icon('shield-check', 13)}
						Before you submit
					</h2>
					<ul class="space-y-4">
						{#each guidelines as point, i}
							<li class="flex gap-4 text-sm font-light leading-relaxed text-[#52525B]">
								<span class="mono mt-0.5 shrink-0 text-[11px] text-[#A1A1AA]">0{i + 1}</span>
								{point}
							</li>
						{/each}
					</ul>
				</div>
			</section>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light leading-relaxed text-[#A1A1AA]">
				Nothing enters the public dataset automatically.
				<br />
				Every approved mapping carries its own provenance.
			</p>
		</div>
	</main>
</div>

<style>
	.page {
		font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
		font-feature-settings: 'ss01' on, 'cv11' on;
	}

	.mono {
		font-family: 'JetBrains Mono', ui-monospace, monospace;
		letter-spacing: 0.02em;
	}

	/* ---- Sections washed with faint light from above ---- */
	.morning {
		background: radial-gradient(ellipse 70% 45% at 50% 0%, rgba(99, 102, 241, 0.045), transparent 65%);
	}

	/* ---- Paper panels: light always falls from above ---- */
	.paper {
		background: #ffffff;
		border: 1px solid #e4e4e7;
		box-shadow:
			inset 0 1px 0 rgba(255, 255, 255, 0.9),
			0 1px 2px rgba(24, 24, 27, 0.04),
			0 16px 32px -20px rgba(24, 24, 27, 0.12);
	}

	/* ---- Ink connectors (matching the landing page chain) ---- */
	.connector {
		display: flex;
		justify-content: center;
		padding: 1.25rem 0;
	}

	.connector-node {
		position: relative;
		z-index: 10;
		display: flex;
		height: 1.75rem;
		width: 1.75rem;
		align-items: center;
		justify-content: center;
		border-radius: 9999px;
		border: 1px solid #e4e4e7;
		background: #ffffff;
		color: #6366f1;
		box-shadow: 0 1px 2px rgba(24, 24, 27, 0.06);
	}

	/* ---- User menu (native details) ---- */
	.user-menu summary::-webkit-details-marker {
		display: none;
	}

	.user-menu[open] summary {
		background: #f4f4f5;
	}

	/* ---- Lunar phase glyphs, drawn in ink (pure CSS) ---- */
	.crescent-sm {
		display: inline-block;
		height: 18px;
		width: 18px;
		border-radius: 9999px;
		box-shadow: inset -5px 3px 0 0 #6366f1;
	}
</style>