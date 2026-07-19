svelte
<!-- src/routes/moderator/history/+page.svelte -->
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
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'arrow-left': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
		search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		'list-filter': '<path d="M3 6h18"/><path d="M7 12h10"/><path d="M10 18h4"/>',
		'arrow-up-down':
			'<path d="m21 16-4 4-4-4"/><path d="M17 20V4"/><path d="m3 8 4-4 4 4"/><path d="M7 4v16"/>',
		eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
		history:
			'<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/>'
	};

	type Decision = 'approved' | 'rejected';

	type ReviewedSubmission = {
		id: string;
		md5: string;
		olid: string;
		title: string;
		author: string;
		score: number;
		decision: Decision;
		reviewedAt: string; // ISO date
	};

	// Realistic Mond data. Replace with load() data in production.
	const moderator = {
		name: 'Jonas Weber',
		email: 'jonas@mailbox.org',
		initials: 'JW'
	};

	const reviewed: ReviewedSubmission[] = [
		{
			id: 'sub_0197',
			md5: 'f2b4d1a9c07e83aa41c69e12',
			olid: 'OL7602281M',
			title: 'The Left Hand of Darkness',
			author: 'Ursula K. Le Guin',
			score: 0.97,
			decision: 'approved',
			reviewedAt: '2025-01-18'
		},
		{
			id: 'sub_0196',
			md5: 'a81c3f5d92be04711fd08c44',
			olid: 'OL24347578M',
			title: 'The Dispossessed',
			author: 'Ursula K. Le Guin',
			score: 0.94,
			decision: 'approved',
			reviewedAt: '2025-01-17'
		},
		{
			id: 'sub_0187',
			md5: '8c1e5d3fa9b2074c6de08b51',
			olid: 'OL7183754M',
			title: 'Invisible Cities',
			author: 'Italo Calvino',
			score: 0.92,
			decision: 'approved',
			reviewedAt: '2025-01-16'
		},
		{
			id: 'sub_0186',
			md5: '5a9f2c7e01d84b36fa2e9c18',
			olid: 'OL32054523M',
			title: 'If on a winter’s night a traveler',
			author: 'Italo Calvino',
			score: 0.71,
			decision: 'rejected',
			reviewedAt: '2025-01-16'
		},
		{
			id: 'sub_0185',
			md5: 'b34e8d1c60f92a75ce4d0f26',
			olid: 'OL24953986M',
			title: 'The Name of the Rose',
			author: 'Umberto Eco',
			score: 0.95,
			decision: 'approved',
			reviewedAt: '2025-01-15'
		},
		{
			id: 'sub_0184',
			md5: '0d7c4b9ea28f13650ab5e794',
			olid: 'OL6990157M',
			title: 'Foucault’s Pendulum',
			author: 'Umberto Eco',
			score: 0.9,
			decision: 'approved',
			reviewedAt: '2025-01-14'
		},
		{
			id: 'sub_0183',
			md5: '7e2a9f5c31d80b64ca1f7d02',
			olid: 'OL26515714M',
			title: 'Pedro Páramo',
			author: 'Juan Rulfo',
			score: 0.58,
			decision: 'rejected',
			reviewedAt: '2025-01-13'
		},
		{
			id: 'sub_0182',
			md5: 'c95b3e7d40a16f28db0c8e63',
			olid: 'OL7360834M',
			title: 'One Hundred Years of Solitude',
			author: 'Gabriel García Márquez',
			score: 0.96,
			decision: 'approved',
			reviewedAt: '2025-01-12'
		},
		{
			id: 'sub_0181',
			md5: '3f6d0a8b92e51c47fe8a2b90',
			olid: 'OL24385514M',
			title: 'Ficciones',
			author: 'Jorge Luis Borges',
			score: 0.66,
			decision: 'rejected',
			reviewedAt: '2025-01-11'
		},
		{
			id: 'sub_0180',
			md5: '1b8e6c2fd7093a54eb6d1c37',
			olid: 'OL7355422M',
			title: 'The Aleph and Other Stories',
			author: 'Jorge Luis Borges',
			score: 0.93,
			decision: 'approved',
			reviewedAt: '2025-01-10'
		}
	];

	const counts = {
		approved: reviewed.filter((r) => r.decision === 'approved').length,
		rejected: reviewed.filter((r) => r.decision === 'rejected').length,
		total: reviewed.length
	};

	const stats: { label: string; value: number; icon: string; accent: 'green' | 'red' | 'ink' }[] = [
		{ label: 'Approved', value: counts.approved, icon: 'check', accent: 'green' },
		{ label: 'Rejected', value: counts.rejected, icon: 'x', accent: 'red' },
		{ label: 'Total reviewed', value: counts.total, icon: 'book-marked', accent: 'ink' }
	];

	const accentStyles: Record<'green' | 'red' | 'ink', string> = {
		green: 'border-[#22C55E]/30 bg-[#22C55E]/10 text-[#16A34A]',
		red: 'border-[#EF4444]/30 bg-[#EF4444]/10 text-[#DC2626]',
		ink: 'border-[#8B5CF6]/30 bg-[#8B5CF6]/10 text-[#6D28D9]'
	};

	const decisionStyles: Record<Decision, string> = {
		approved: 'border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]',
		rejected: 'border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]'
	};

	const decisionLabels: Record<Decision, string> = {
		approved: 'Approved',
		rejected: 'Rejected'
	};

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

{#snippet decisionBadge(decision: Decision)}
	<span
		class="inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-[11px] {decisionStyles[decision]}"
	>
		{decisionLabels[decision]}
	</span>
{/snippet}

{#snippet viewButton(id: string, title: string)}
	<a
		href="/moderator/review/{id}"
		class="inline-flex items-center gap-1.5 rounded-md border border-[#E4E4E7] bg-white px-3 py-1.5 text-xs text-[#3F3F46] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05] hover:text-[#6D28D9]"
		aria-label="View review of: {title}"
	>
		{@render icon('eye', 12)}
		View
	</a>
{/snippet}

<svelte:head>
	<title>Moderation History — Mond</title>
	<meta
		name="description"
		content="Browse your recently reviewed mappings and revisit past moderation decisions."
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
			<section aria-labelledby="history-heading">
				<a
					href="/moderator"
					class="mb-8 inline-flex items-center gap-2 text-sm font-light text-[#71717A] transition-colors hover:text-[#18181B]"
				>
					{@render icon('arrow-left', 14)}
					Back to queue
				</a>

				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Moderation history
				</p>
				<h1
					id="history-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Reviewed Submissions
				</h1>
				<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
					Browse your recently reviewed mappings and revisit past moderation
					decisions.
				</p>
			</section>

			<!-- ============ STATISTICS ============ -->
			<section aria-label="Review statistics" class="mt-12">
				<dl class="grid grid-cols-3 gap-4">
					{#each stats as stat}
						<div class="paper rounded-lg p-5 sm:p-6">
							<div class="flex items-center justify-between">
								<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
									{stat.label}
								</dt>
								<span
									class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full border {accentStyles[stat.accent]}"
								>
									{@render icon(stat.icon, 12, 2)}
								</span>
							</div>
							<dd class="mono mt-4 text-3xl font-light text-[#18181B]">
								{stat.value}
							</dd>
						</div>
					{/each}
				</dl>
			</section>

			<!-- ============ FILTERS ============ -->
			<section aria-label="Filter history" class="mt-8">
				<div class="paper rounded-lg p-5 sm:p-6">
					<div class="flex flex-col gap-4 lg:flex-row lg:items-end">
						<!-- Search -->
						<div class="flex-1">
							<label
								for="history-search"
								class="mb-2 block text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]"
							>
								Search
							</label>
							<div class="relative">
								<span
									class="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[#A1A1AA]"
								>
									{@render icon('search', 14)}
								</span>
								<input
									id="history-search"
									type="search"
									placeholder="Title, MD5 or OLID…"
									class="w-full rounded-md border border-[#E4E4E7] bg-[#FAFAFA] py-2.5 pl-10 pr-4 text-sm font-light text-[#3F3F46] placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/40 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
								/>
							</div>
						</div>

						<!-- Status filter -->
						<div class="lg:w-48">
							<label
								for="history-status"
								class="mb-2 block text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]"
							>
								Status
							</label>
							<div class="relative">
								<span
									class="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[#A1A1AA]"
								>
									{@render icon('list-filter', 14)}
								</span>
								<select
									id="history-status"
									class="w-full appearance-none rounded-md border border-[#E4E4E7] bg-[#FAFAFA] py-2.5 pl-10 pr-9 text-sm font-light text-[#3F3F46] focus:border-[#8B5CF6]/40 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
								>
									<option>All</option>
									<option>Approved</option>
									<option>Rejected</option>
								</select>
								<span
									class="pointer-events-none absolute right-3.5 top-1/2 -translate-y-1/2 text-[#A1A1AA]"
								>
									{@render icon('chevron-down', 14)}
								</span>
							</div>
						</div>

						<!-- Sort -->
						<div class="lg:w-48">
							<label
								for="history-sort"
								class="mb-2 block text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]"
							>
								Sort by
							</label>
							<div class="relative">
								<span
									class="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[#A1A1AA]"
								>
									{@render icon('arrow-up-down', 14)}
								</span>
								<select
									id="history-sort"
									class="w-full appearance-none rounded-md border border-[#E4E4E7] bg-[#FAFAFA] py-2.5 pl-10 pr-9 text-sm font-light text-[#3F3F46] focus:border-[#8B5CF6]/40 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
								>
									<option>Most recent</option>
								</select>
								<span
									class="pointer-events-none absolute right-3.5 top-1/2 -translate-y-1/2 text-[#A1A1AA]"
								>
									{@render icon('chevron-down', 14)}
								</span>
							</div>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ HISTORY ============ -->
			<section aria-labelledby="record-heading" class="mt-12">
				<div class="mb-6">
					<p class="mb-2 text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]">
						— The record of your decisions —
					</p>
					<h2 id="record-heading" class="text-xl font-extralight tracking-tight text-[#18181B]">
						Review history
					</h2>
				</div>

				{#if reviewed.length === 0}
					<!-- Empty state -->
					<div class="paper rounded-lg px-8 py-20 text-center">
						<div class="mx-auto mb-6 flex justify-center">
							<span class="phase-crescent" aria-hidden="true"></span>
						</div>
						<h3 class="text-lg font-extralight tracking-tight text-[#18181B]">
							You haven’t reviewed any submissions yet.
						</h3>
						<p class="quote mx-auto mt-3 max-w-sm text-[15px] leading-relaxed text-[#71717A]">
							“Careful eyes are the archive’s real infrastructure.”
						</p>
						<div class="mt-8">
							<a
								href="/moderator"
								class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
							>
								{@render icon('shield-check', 15)}
								Return to Review Queue
							</a>
						</div>
					</div>
				{:else}
					<!-- Desktop: table -->
					<div class="paper hidden overflow-hidden rounded-lg md:block">
						<table class="w-full text-left">
							<caption class="sr-only">
								Your reviewed mapping submissions with validation score, decision and review date
							</caption>
							<thead>
								<tr class="border-b border-[#F4F4F5]">
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Title
									</th>
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
										Decision
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Reviewed on
									</th>
									<th scope="col" class="px-6 py-4 text-right">
										<span class="sr-only">Actions</span>
									</th>
								</tr>
							</thead>
							<tbody>
								{#each reviewed as review (review.id)}
									<tr class="border-b border-[#F4F4F5] transition-colors last:border-0 hover:bg-[#FAFAFA]">
										<td class="px-6 py-4">
											<span class="block text-sm font-light text-[#18181B]">
												{review.title}
											</span>
											<span class="mt-0.5 block text-xs font-light text-[#A1A1AA]">
												{review.author}
											</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#3F3F46]" title={review.md5}>
												{truncateMd5(review.md5)}
											</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#6366F1]">{review.olid}</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#3F3F46]">
												{review.score.toFixed(2)}
											</span>
										</td>
										<td class="px-6 py-4">
											{@render decisionBadge(review.decision)}
										</td>
										<td class="px-6 py-4">
											<time
												datetime={review.reviewedAt}
												class="text-sm font-light text-[#71717A]"
											>
												{formatDate(review.reviewedAt)}
											</time>
										</td>
										<td class="px-6 py-4 text-right">
											{@render viewButton(review.id, review.title)}
										</td>
									</tr>
								{/each}
							</tbody>
						</table>
					</div>

					<!-- Mobile: stacked cards -->
					<ul class="space-y-4 md:hidden">
						{#each reviewed as review (review.id)}
							<li class="paper rounded-lg p-5">
								<div class="flex items-start justify-between gap-4">
									<div>
										<p class="text-sm font-light text-[#18181B]">{review.title}</p>
										<p class="mt-0.5 text-xs font-light text-[#A1A1AA]">{review.author}</p>
										<p class="mono mt-1.5 text-xs text-[#A1A1AA]" title={review.md5}>
											{truncateMd5(review.md5)}
										</p>
									</div>
									{@render decisionBadge(review.decision)}
								</div>
								<dl class="mt-4 grid grid-cols-3 gap-3 border-t border-[#F4F4F5] pt-4">
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">OLID</dt>
										<dd class="mono mt-1 text-xs text-[#6366F1]">{review.olid}</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Score</dt>
										<dd class="mono mt-1 text-xs text-[#3F3F46]">{review.score.toFixed(2)}</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Reviewed</dt>
										<dd class="mt-1 text-xs font-light text-[#71717A]">
											<time datetime={review.reviewedAt}>{formatDate(review.reviewedAt)}</time>
										</dd>
									</div>
								</dl>
								<div class="mt-4 flex justify-end border-t border-[#F4F4F5] pt-4">
									{@render viewButton(review.id, review.title)}
								</div>
							</li>
						{/each}
					</ul>
				{/if}
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

	.phase-crescent {
		display: inline-block;
		height: 32px;
		width: 32px;
		border-radius: 9999px;
		box-shadow: inset -9px 5px 0 0 #6366f1;
	}
</style>