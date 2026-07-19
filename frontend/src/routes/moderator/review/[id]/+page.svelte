svelte
<!-- src/routes/moderator/review/[id]/+page.svelte -->
<script lang="ts">
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'layout-dashboard':
			'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
		'file-down':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
		settings:
			'<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
		'shield-check':
			'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
		check: '<path d="M20 6 9 17l-5-5"/>',
		x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
		'triangle-alert':
			'<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
		'search-check':
			'<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'arrow-left': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
		library: '<path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/>',
		'pen-line':
			'<path d="M12 20h9"/><path d="M16.376 3.622a1 1 0 0 1 3.002 3.002L7.368 18.635a2 2 0 0 1-.855.506l-2.872.838a.5.5 0 0 1-.62-.62l.838-2.872a2 2 0 0 1 .506-.854z"/>'
	};

	type Field = {
		label: string;
		aa: string;
		ol: string;
		mono?: boolean;
		match: boolean;
	};

	// Realistic Mond data. Replace with load() data in production.
	const moderator = {
		name: 'Jonas Weber',
		email: 'jonas@mailbox.org',
		initials: 'JW'
	};

	const submission = {
		id: 'sub_0195',
		contributor: 'lena.hoffmann',
		submittedAt: '2025-01-16',
		score: 0.97,
		md5: '4de90bb7215fa3c8e6a1d270f8e3b19c',
		olid: 'OL26331930M'
	};

	// Field-by-field comparison. Publisher differs (imprint vs parent),
	// everything else matches after normalization.
	const fields: Field[] = [
		{
			label: 'Title',
			aa: 'A Wizard of Earthsea',
			ol: 'A Wizard of Earthsea',
			match: true
		},
		{
			label: 'Authors',
			aa: 'Ursula K. Le Guin',
			ol: 'Ursula K. Le Guin',
			match: true
		},
		{
			label: 'Language',
			aa: 'English',
			ol: 'English',
			match: true
		},
		{
			label: 'Publisher',
			aa: 'Bantam Books',
			ol: 'Bantam Spectra',
			match: false
		},
		{
			label: 'Year',
			aa: '1984',
			ol: '1984',
			match: true
		},
		{
			label: 'ISBN-13',
			aa: '978-0-553-26250-7',
			ol: '978-0-553-26250-7',
			mono: true,
			match: true
		},
		{
			label: 'ISBN-10',
			aa: '0-553-26250-5',
			ol: '0-553-26250-5',
			mono: true,
			match: true
		}
	];

	const validationChecks: { label: string; passed: boolean }[] = [
		{ label: 'Title normalized and matched', passed: true },
		{ label: 'Author name matched', passed: true },
		{ label: 'ISBN-13 checksum valid', passed: true },
		{ label: 'Publication year matched', passed: true }
	];

	let notes = $state('');

	function truncateMd5(md5: string): string {
		return `${md5.slice(0, 8)}…${md5.slice(-4)}`;
	}

	function formatDate(iso: string): string {
		return new Date(iso + 'T00:00:00').toLocaleDateString('en-GB', {
			day: 'numeric',
			month: 'short',
			year: 'numeric'
		});
	}
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

{#snippet mismatchBadge()}
	<span
		class="inline-flex items-center gap-1 rounded-full border border-[#F59E0B]/40 bg-[#F59E0B]/10 px-2 py-0.5 text-[10px] text-[#B45309]"
	>
		{@render icon('triangle-alert', 9, 2)}
		Differs
	</span>
{/snippet}

{#snippet recordField(field: Field, value: string, flagged: boolean)}
	<div class="flex items-baseline justify-between gap-6 py-3 first:pt-0 last:pb-0">
		<dt class="shrink-0 text-[11px] tracking-[0.2em] uppercase text-[#A1A1AA]">
			{field.label}
		</dt>
		<dd class="flex items-baseline gap-2 text-right">
			{#if flagged}
				{@render mismatchBadge()}
			{/if}
			<span
				class="{field.mono ? 'mono' : 'font-light'} text-sm {flagged
					? 'text-[#B45309]'
					: 'text-[#3F3F46]'}"
			>
				{value}
			</span>
		</dd>
	</div>
{/snippet}

<svelte:head>
	<title>Review {submission.id} — Mond</title>
	<meta
		name="description"
		content="Compare both records carefully before making a moderation decision."
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
						href="/moderator"
						aria-current="page"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#18181B]"
					>
						{@render icon('shield-check', 15)}
						Moderation
					</a>
					<a
						href="/dataset"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
					>
						{@render icon('file-down', 15)}
						Dataset
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
					aria-label="Account menu for {moderator.name}"
				>
					<span
						class="flex h-8 w-8 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] text-xs font-medium text-[#6D28D9]"
					>
						{moderator.initials}
					</span>
					<span class="hidden text-sm font-light text-[#3F3F46] sm:inline">{moderator.name}</span>
					<span class="text-[#A1A1AA]">{@render icon('chevron-down', 14)}</span>
				</summary>

				<div
					class="paper absolute right-0 z-30 mt-2 w-56 overflow-hidden rounded-lg py-1.5"
					role="menu"
				>
					<div class="border-b border-[#F4F4F5] px-4 py-3">
						<p class="text-sm text-[#18181B]">{moderator.name}</p>
						<p class="mono mt-0.5 text-xs text-[#A1A1AA]">{moderator.email}</p>
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
	</header>

	<main class="morning">
		<div class="mx-auto max-w-6xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ HEADER ============ -->
			<section aria-labelledby="review-heading">
				<a
					href="/moderator"
					class="mb-8 inline-flex items-center gap-2 text-sm font-light text-[#71717A] transition-colors hover:text-[#18181B]"
				>
					{@render icon('arrow-left', 14)}
					Back to queue
				</a>

				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Moderator review
				</p>
				<h1
					id="review-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Review Submission
				</h1>
				<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
					Compare both records carefully before making a moderation decision.
				</p>

				<!-- Submission meta -->
				<dl class="mt-8 flex flex-wrap gap-x-10 gap-y-4 border-t border-[#E4E4E7] pt-6">
					<div>
						<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Submission</dt>
						<dd class="mono mt-1 text-sm text-[#3F3F46]">{submission.id}</dd>
					</div>
					<div>
						<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Contributor</dt>
						<dd class="mono mt-1 text-sm text-[#3F3F46]">{submission.contributor}</dd>
					</div>
					<div>
						<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Submitted</dt>
						<dd class="mt-1 text-sm font-light text-[#3F3F46]">
							<time datetime={submission.submittedAt}>{formatDate(submission.submittedAt)}</time>
						</dd>
					</div>
					<div>
						<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Validation score</dt>
						<dd class="mono mt-1 text-sm text-[#6D28D9]">{submission.score.toFixed(2)}</dd>
					</div>
				</dl>
			</section>

			<!-- ============ RECORD COMPARISON ============ -->
			<section aria-label="Record comparison" class="mt-12">
				<div class="grid gap-6 lg:grid-cols-2">
					<!-- Left: Anna's Archive -->
					<article class="paper rounded-lg p-6 sm:p-8" aria-labelledby="aa-heading">
						<div class="mb-6 flex items-center justify-between border-b border-[#F4F4F5] pb-5">
							<h2
								id="aa-heading"
								class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
							>
								{@render icon('book-marked', 13)}
								Anna’s Archive
							</h2>
							<span class="mono text-[11px] text-[#A1A1AA]">source</span>
						</div>

						<dl class="divide-y divide-[#F4F4F5]">
							{#each fields as field}
								{@render recordField(field, field.aa, false)}
							{/each}
							<div class="flex items-baseline justify-between gap-6 py-3 last:pb-0">
								<dt class="shrink-0 text-[11px] tracking-[0.2em] uppercase text-[#A1A1AA]">
									MD5
								</dt>
								<dd class="mono text-sm text-[#3F3F46]" title={submission.md5}>
									{truncateMd5(submission.md5)}
								</dd>
							</div>
						</dl>
					</article>

					<!-- Right: Open Library -->
					<article class="paper rounded-lg p-6 sm:p-8" aria-labelledby="ol-heading">
						<div class="mb-6 flex items-center justify-between border-b border-[#F4F4F5] pb-5">
							<h2
								id="ol-heading"
								class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
							>
								{@render icon('library', 13)}
								Open Library
							</h2>
							<span class="mono text-[11px] text-[#A1A1AA]">target</span>
						</div>

						<dl class="divide-y divide-[#F4F4F5]">
							{#each fields as field}
								{@render recordField(field, field.ol, !field.match)}
							{/each}
							<div class="flex items-baseline justify-between gap-6 py-3 last:pb-0">
								<dt class="shrink-0 text-[11px] tracking-[0.2em] uppercase text-[#A1A1AA]">
									OLID
								</dt>
								<dd class="mono text-sm text-[#6366F1]">{submission.olid}</dd>
							</div>
						</dl>
					</article>
				</div>
			</section>

			<!-- ============ VALIDATION SUMMARY ============ -->
			<section aria-labelledby="validation-heading" class="mt-8">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6">
						<h2
							id="validation-heading"
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							{@render icon('search-check', 13)}
							Validation summary
						</h2>
					</div>

					<div class="flex flex-col gap-8 sm:flex-row sm:items-center sm:justify-between">
						<ul class="space-y-3">
							{#each validationChecks as check}
								<li class="flex items-center gap-3 text-sm font-light text-[#3F3F46]">
									<span
										class="flex h-4 w-4 shrink-0 items-center justify-center rounded-full border {check.passed
											? 'border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]'
											: 'border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]'}"
									>
										{@render icon(check.passed ? 'check' : 'x', 9, 2.5)}
									</span>
									{check.label}
								</li>
							{/each}
						</ul>

						<div
							class="shrink-0 rounded-lg border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.05] px-10 py-8 text-center sm:ml-10"
						>
							<p class="text-[10px] tracking-[0.25em] uppercase text-[#6D28D9]">
								Overall confidence
							</p>
							<p class="mono mt-3 text-4xl font-light text-[#6D28D9]">97%</p>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ MODERATOR NOTES ============ -->
			<section aria-labelledby="notes-heading" class="mt-8">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-5">
						<h2 id="notes-heading" class="sr-only">Moderator notes</h2>
						<label
							for="moderator-notes"
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							{@render icon('pen-line', 13)}
							Moderator notes
						</label>
					</div>
					<textarea
						id="moderator-notes"
						bind:value={notes}
						rows="6"
						placeholder="Explain your decision..."
						class="w-full resize-y rounded-md border border-[#E4E4E7] bg-[#FAFAFA] px-4 py-3.5 text-sm font-light leading-relaxed text-[#3F3F46] placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/40 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
					></textarea>
					<p class="mt-3 text-xs font-light text-[#A1A1AA]">
						Your note becomes part of the permanent moderation record for this mapping.
					</p>
				</div>
			</section>

			<!-- ============ DECISION ============ -->
			<section aria-labelledby="decision-heading" class="mt-8">
				<div class="paper sealed rounded-lg p-8 sm:p-10">
					<div class="text-center sm:flex sm:items-center sm:justify-between sm:text-left">
						<div>
							<p class="text-[11px] tracking-[0.25em] uppercase text-[#6D28D9]">
								Decision
							</p>
							<h2
								id="decision-heading"
								class="mt-3 text-2xl font-extralight tracking-tight text-[#18181B]"
							>
								Seal the record.
							</h2>
							<p class="mt-2 max-w-md text-sm font-light leading-relaxed text-[#52525B]">
								Approved mappings enter the public dataset — permanent, attributed,
								and free. When in doubt, reject.
							</p>
						</div>

						<div
							class="mt-8 flex flex-col items-stretch gap-3 sm:mt-0 sm:ml-10 sm:shrink-0 sm:flex-row sm:items-center"
						>
							<button
								type="button"
								class="inline-flex items-center justify-center gap-2.5 rounded-md border border-[#22C55E]/40 bg-[#22C55E]/10 px-7 py-3.5 text-sm text-[#16A34A] transition-colors hover:bg-[#22C55E]/[0.18]"
							>
								{@render icon('check', 15, 2)}
								Approve Mapping
							</button>
							<button
								type="button"
								class="inline-flex items-center justify-center gap-2.5 rounded-md border border-[#EF4444]/30 bg-white px-7 py-3.5 text-sm text-[#DC2626] transition-colors hover:bg-[#EF4444]/[0.06]"
							>
								{@render icon('x', 15, 2)}
								Reject Mapping
							</button>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light text-[#A1A1AA]">
				Every moderation decision is recorded. The dataset carries its own provenance.
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

	.paper.sealed {
		border-color: rgba(139, 92, 246, 0.35);
		background: linear-gradient(to bottom, rgba(139, 92, 246, 0.04), #ffffff 45%);
		box-shadow:
			inset 0 1px 0 rgba(255, 255, 255, 0.9),
			0 0 48px -14px rgba(139, 92, 246, 0.25),
			0 16px 32px -20px rgba(24, 24, 27, 0.12);
	}

	/* ---- User menu (native details) ---- */
	.user-menu summary::-webkit-details-marker {
		display: none;
	}

	.user-menu[open] summary {
		background: #f4f4f5;
	}

	/* ---- Lunar phase glyph, drawn in ink (pure CSS) ---- */
	.crescent-sm {
		display: inline-block;
		height: 18px;
		width: 18px;
		border-radius: 9999px;
		box-shadow: inset -5px 3px 0 0 #6366f1;
	}
</style>