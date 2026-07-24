
<script lang="ts">
import { goto } from "$app/navigation";
import { onMount } from "svelte";

import { user, authLoading } from "$lib/stores/auth";

import {
	getSubmissionHistory,
	getSubmissionStats
} from "$lib/api/submit";

import type {
	SubmissionHistoryItem,
	SubmissionStats
} from "$lib/types/submit";
// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'layout-dashboard':
			'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
		'file-down':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
		settings:
			'<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
		check: '<path d="M20 6 9 17l-5-5"/>',
		x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
		hourglass:
			'<path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/>',
		library: '<path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/>',
		upload:
			'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>',
		plus: '<path d="M5 12h14"/><path d="M12 5v14"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
		'arrow-up-right': '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>'
	};
type SubmissionStatus = "pending" | "approved" | "rejected";

let submissions = $state<SubmissionHistoryItem[]>([]);
let stats = $state<SubmissionStats | null>(null);

let loading = $state(true);
let error = $state("");

async function loadDashboard() {
	loading = true;
	error = "";

	try {
		const [history, dashboardStats] = await Promise.all([
			getSubmissionHistory(),
			getSubmissionStats()
		]);

		console.log(history);

		submissions = [...history];
		stats = { ...dashboardStats };
	}
	catch (e) {
		console.error(e);
		error = "Failed to load dashboard.";
	}
	finally {
		loading = false;
	}
}

function getInitials(name: string) {
	return name
		.split(" ")
		.map((p) => p[0])
		.join("")
		.slice(0, 2)
		.toUpperCase();
}

function truncateMd5(md5: string) {
	return `${md5.slice(0, 8)}…${md5.slice(-4)}`;
}

function formatDate(date: string) {
	return new Date(date).toLocaleDateString("en-GB", {
		day: "numeric",
		month: "short",
		year: "numeric"
	});
}

onMount(loadDashboard);

$effect(() => {
	if (!$authLoading && !$user) {
		goto("/login");
	}
});

const statusStyles: Record<SubmissionStatus, string> = {
	approved: "border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]",
	pending: "border-[#F59E0B]/40 bg-[#F59E0B]/10 text-[#B45309]",
	rejected: "border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]"
};

const statusLabels: Record<SubmissionStatus, string> = {
	approved: "Approved",
	pending: "Pending",
	rejected: "Rejected"
};
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

{#snippet statusBadge(status: SubmissionStatus)}
	<span
		class="inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-[11px] {statusStyles[status]}"
	>
		{statusLabels[status]}
	</span>
{/snippet}

{#snippet statCard(label: string, value: number, iconName: string, accent: string, iconBox: string)}
	<div class="paper rounded-lg p-5 sm:p-6">
		<div class="flex items-start justify-between">
			<dt class="text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
				{label}
			</dt>
			<span
				class="flex h-8 w-8 shrink-0 items-center justify-center rounded-full border {iconBox}"
				aria-hidden="true"
			>
				{@render icon(iconName, 14)}
			</span>
		</div>
		<dd class="mono mt-3 text-3xl font-extralight tracking-tight {accent}">
			{value}
		</dd>
	</div>
{/snippet}

<svelte:head>
	<title>Dashboard — Mond</title>
	<meta name="description" content="Your Mond contributor dashboard. Track submissions, review outcomes, and submit new mappings." />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&family=Newsreader:ital,wght@1,300&family=JetBrains+Mono:wght@300;400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="page min-h-screen bg-[#FAFAFA] text-[#18181B] antialiased">
	<!-- ============ NAV ============ -->
	<header class="sticky top-0 z-20 border-b border-[#E4E4E7] bg-white/85 backdrop-blur-sm">
		<nav class="mx-auto flex max-w-6xl items-center justify-between px-6 py-4" aria-label="Primary">
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
						aria-current="page"
						class="nav-link nav-link--active flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#18181B]"
					>
						{@render icon('layout-dashboard', 15)}
						Dashboard
					</a>

					

					<a
						href="/dashboard/settings"
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
						aria-hidden="true"
					>
						{$user ? getInitials($user.username) : ""}
					</span>
					<span class="hidden text-sm font-light text-[#3F3F46] sm:inline">{$user?.username}</span>
					<span class="text-[#A1A1AA]" aria-hidden="true">{@render icon('chevron-down', 14)}</span>
				</summary>

				<div
					class="paper absolute right-0 z-30 mt-2 w-56 overflow-hidden rounded-lg py-1.5"
					role="menu"
				>
					<div class="border-b border-[#F4F4F5] px-4 py-3">
						<p class="text-sm text-[#18181B]">{$user?.username}</p>
						<p class="mono mt-0.5 truncate text-xs text-[#A1A1AA]">{$user?.email}</p>
					</div>
					<a
						href="/dashboard/settings"
						role="menuitem"
						class="flex items-center gap-2.5 px-4 py-2.5 text-sm font-light text-[#3F3F46] transition-colors hover:bg-[#F4F4F5]"
					>
						{@render icon('user', 14)}
						Profile &amp; settings
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
		<nav class="flex items-center gap-1 overflow-x-auto border-t border-[#F4F4F5] px-6 py-2 sm:hidden" aria-label="Primary mobile">
			<a
				href="/dashboard"
				aria-current="page"
				class="nav-link nav-link--active flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#18181B]"
			>
				{@render icon('layout-dashboard', 14)}
				Dashboard
			</a>
			
			<a
				href="/dashboard/settings"
				class="flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('settings', 14)}
				Settings
			</a>
		</nav>
	</header>

	<main class="morning">
		<div class="mx-auto max-w-6xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ WELCOME ============ -->
			<section aria-labelledby="welcome-heading">
				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Contributor dashboard
				</p>
				<div class="flex flex-col gap-8 sm:flex-row sm:items-end sm:justify-between">
					<div>
						<h1
							id="welcome-heading"
							class="text-balance text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
						>
							Welcome back.
						</h1>
						<p class="mt-4 max-w-lg text-pretty text-sm font-light leading-relaxed text-[#52525B]">
							Your mappings connect MD5 records to Open Library editions.
							Every submission passes through validation and human review before it
							enters the public dataset.
						</p>
					</div>
					<div class="shrink-0">
						
					</div>
				</div>
			</section>

			<!-- ============ ERROR ============ -->
			{#if error}
				<div
					role="alert"
					class="mt-10 flex items-center gap-3 rounded-lg border border-[#EF4444]/40 bg-[#EF4444]/[0.06] px-5 py-4 text-sm font-light text-[#DC2626]"
				>
					{@render icon('x', 15)}
					{error}
				</div>
			{/if}

			<!-- ============ STATISTICS ============ -->
			<section aria-labelledby="stats-heading" class="mt-12">
				<h2 id="stats-heading" class="sr-only">Submission statistics</h2>

				{#if loading && !stats}
					<!-- Loading skeleton -->
					<div class="grid grid-cols-2 gap-4 lg:grid-cols-4" aria-hidden="true">
						{#each Array(4) as _}
							<div class="paper rounded-lg p-5 sm:p-6">
								<div class="shimmer h-3 w-16 rounded"></div>
								<div class="shimmer mt-4 h-8 w-12 rounded"></div>
							</div>
						{/each}
					</div>
					<p class="sr-only" role="status">Loading dashboard…</p>
				{:else if stats}
					<dl class="grid grid-cols-2 gap-4 lg:grid-cols-4">
						{@render statCard(
							'Pending',
							stats.pending,
							'hourglass',
							'text-[#B45309]',
							'border-[#F59E0B]/40 bg-[#F59E0B]/10 text-[#B45309]'
						)}
						{@render statCard(
							'Approved',
							stats.approved,
							'check',
							'text-[#16A34A]',
							'border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]'
						)}
						{@render statCard(
							'Rejected',
							stats.rejected,
							'x',
							'text-[#DC2626]',
							'border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]'
						)}
						{@render statCard(
							'Total',
							stats.total,
							'library',
							'text-[#18181B]',
							'border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] text-[#6D28D9]'
						)}
					</dl>
				{/if}
			</section>

			<!-- ============ PRIMARY ACTION ============ -->
			<section aria-labelledby="submit-heading" class="mt-12">
				<div
					class="paper sealed rounded-lg p-8 text-center sm:flex sm:items-center sm:justify-between sm:p-10 sm:text-left"
				>
					<div>
						<p class="text-[11px] tracking-[0.25em] uppercase text-[#6D28D9]">
							Contribute
						</p>
						<h2
							id="submit-heading"
							class="mt-3 text-2xl font-extralight tracking-tight text-[#18181B]"
						>
							Submit a new mapping.
						</h2>
						<p class="mt-2 max-w-md text-pretty text-sm font-light leading-relaxed text-[#52525B]">
							Link an MD5 record to an Open Library edition. Validation
							runs instantly; a moderator reviews it within days.
						</p>
					</div>
					<div class="mt-8 sm:mt-0 sm:ml-10 sm:shrink-0">
						<a
							href="/dashboard/submit"
							class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-7 py-3.5 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
						>
							{@render icon('upload', 15)}
							New mapping
						</a>
					</div>
				</div>
			</section>

			<!-- ============ RECENT SUBMISSIONS ============ -->
			<section aria-labelledby="recent-heading" class="mt-16">
				<div class="mb-6 flex items-end justify-between">
					<div>
						<p class="mb-2 text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]">
							— Your record —
						</p>
						<h2 id="recent-heading" class="text-xl font-extralight tracking-tight text-[#18181B]">
							Recent submissions
						</h2>
					</div>
					<a
						href="/submissions"
						class="flex items-center gap-1.5 text-sm font-light text-[#71717A] transition-colors hover:text-[#18181B]"
					>
						View all
						{@render icon('arrow-up-right', 13)}
					</a>
				</div>

				{#if loading && submissions.length === 0}
					<!-- Loading skeleton -->
					<div class="paper rounded-lg p-6" aria-hidden="true">
						<div class="space-y-5">
							{#each Array(3) as _}
								<div class="flex items-center justify-between gap-6">
									<div class="flex-1 space-y-2">
										<div class="shimmer h-3.5 w-40 rounded"></div>
										<div class="shimmer h-3 w-24 rounded"></div>
									</div>
									<div class="shimmer h-5 w-20 rounded-full"></div>
								</div>
							{/each}
						</div>
					</div>
				{:else if submissions.length === 0}
					<!-- Empty state -->
					<div class="paper rounded-lg px-8 py-20 text-center">
						<div class="mx-auto mb-6 flex justify-center">
							<span class="phase-crescent" aria-hidden="true"></span>
						</div>
						<h3 class="text-lg font-extralight tracking-tight text-[#18181B]">
							Nothing here yet.
						</h3>
						<p class="quote mx-auto mt-3 max-w-sm text-[15px] leading-relaxed text-[#71717A]">
							“Every archive begins with a single record.”
						</p>
						<div class="mt-8">
							<a
								href="/dashboard/submit"
								class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
							>
								{@render icon('upload', 15)}
								Submit your first mapping
							</a>
						</div>
					</div>
				{:else}
					<!-- Desktop: table -->
					<div class="paper hidden overflow-hidden rounded-lg md:block">
						<table class="w-full text-left">
							<caption class="sr-only">
								Your recent mapping submissions with validation score and review status
							</caption>
							<thead>
								<tr class="border-b border-[#F4F4F5]">
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										MD5
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										OLID
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Score
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Status
									</th>
									<th scope="col" class="px-6 py-4 text-right text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Submitted
									</th>
								</tr>
							</thead>
							<tbody>
								{#each submissions as submission (submission.id)}
									<tr class="border-b border-[#F4F4F5] transition-colors last:border-0 hover:bg-[#FAFAFA]">
										<td class="px-6 py-4">
											<span class="mono block text-sm text-[#3F3F46]" title={submission.md5}>
												{truncateMd5(submission.md5)}
											</span>
											<span class="mt-0.5 block text-xs font-light text-[#A1A1AA]">
												{submission.title}
											</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#6366F1]">{submission.olid}</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#3F3F46]">
												{submission.validation_score.toFixed(2)}
											</span>
										</td>
										<td class="px-6 py-4">
											{@render statusBadge(submission.status)}
										</td>
										<td class="px-6 py-4 text-right">
											<time
												datetime={submission.submitted_at}
												class="text-sm font-light text-[#71717A]"
											>
												{formatDate(submission.submitted_at)}
											</time>
										</td>
									</tr>
								{/each}
							</tbody>
						</table>
					</div>

					<!-- Mobile: stacked cards -->
					<ul class="space-y-4 md:hidden">
						{#each submissions as submission (submission.id)}
							<li class="paper rounded-lg p-5">
								<div class="flex items-start justify-between gap-4">
									<div class="min-w-0">
										<p class="truncate text-sm font-light text-[#18181B]">{submission.title}</p>
										<p class="mono mt-1 text-xs text-[#A1A1AA]" title={submission.md5}>
											{truncateMd5(submission.md5)}
										</p>
									</div>
									{@render statusBadge(submission.status)}
								</div>
								<dl class="mt-4 grid grid-cols-3 gap-3 border-t border-[#F4F4F5] pt-4">
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">OLID</dt>
										<dd class="mono mt-1 text-xs text-[#6366F1]">{submission.olid}</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Score</dt>
										<dd class="mono mt-1 text-xs text-[#3F3F46]">{submission.validation_score.toFixed(2)}</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Submitted</dt>
										<dd class="mt-1 text-xs font-light text-[#71717A]">
											<time datetime={submission.submitted_at}>{formatDate(submission.submitted_at)}</time>
										</dd>
									</div>
								</dl>
							</li>
						{/each}
					</ul>
				{/if}
			</section>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light text-[#A1A1AA]">
				Approved mappings enter the public dataset — permanent, attributed.
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

	.quote {
		font-family: 'Newsreader', Georgia, serif;
		font-style: italic;
		font-weight: 300;
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

	/* ---- Active nav item: a quiet underline of ink ---- */
	.nav-link--active {
		position: relative;
	}

	.nav-link--active::after {
		content: '';
		position: absolute;
		left: 0.75rem;
		right: 0.75rem;
		bottom: 0.15rem;
		height: 1px;
		background: linear-gradient(to right, transparent, rgba(99, 102, 241, 0.6), transparent);
	}

	/* ---- User menu (native details) ---- */
	.user-menu summary::-webkit-details-marker {
		display: none;
	}

	.user-menu[open] summary {
		background: #f4f4f5;
	}

	/* ---- Loading shimmer: pale moonlight passing over paper ---- */
	.shimmer {
		background: linear-gradient(
			90deg,
			#f4f4f5 25%,
			#eeeef2 50%,
			#f4f4f5 75%
		);
		background-size: 200% 100%;
		animation: shimmer 1.6s ease-in-out infinite;
	}

	@keyframes shimmer {
		0% {
			background-position: 200% 0;
		}
		100% {
			background-position: -200% 0;
		}
	}

	@media (prefers-reduced-motion: reduce) {
		.shimmer {
			animation: none;
		}
	}

	/* ---- Lunar phase glyphs, drawn in ink (pure CSS) ---- */
	.crescent-sm {
		display: inline-block;
		height: 18px;
		width: 18px;
		border-radius: 9999px;
		box-shadow: inset -5px 3px 0 0 #6366f1;
	}

	.phase-crescent {
		display: inline-block;
		height: 32px;
		width: 32px;
		border-radius: 9999px;
		box-shadow: inset -9px 5px 0 0 #6366f1;
	}
</style>