svelte
<!-- src/routes/moderator/queue/+page.svelte -->
<script lang="ts">
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'layout-dashboard':
			'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
		'shield-check':
			'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
		'file-down':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
		settings:
			'<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
		check: '<path d="M20 6 9 17l-5-5"/>',
		hourglass:
			'<path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/>',
		gauge:
			'<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
		'calendar-clock':
			'<path d="M21 7.5V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h3.5"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h5"/><path d="M17.5 17.5 16 16.25V14"/><path d="M22 16a6 6 0 1 1-12 0 6 6 0 0 1 12 0Z"/>',
		search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'arrow-up-right': '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
		filter:
			'<polygon points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"/>'
	};

	type PendingSubmission = {
		id: string;
		title: string;
		contributor: string;
		md5: string;
		olid: string;
		score: number;
		submittedAt: string; // ISO date
	};

	type Stat = {
		label: string;
		value: string;
		icon: string;
		accent: 'amber' | 'green' | 'ink' | 'neutral';
	};

	// Realistic Mond data. Replace with load() data in production.
	const moderator = {
		name: 'Jonas Weber',
		email: 'jonas@mailbox.org',
		initials: 'JW'
	};

	const queue: PendingSubmission[] = [
		{
			id: 'sub_0201',
			title: 'A Wizard of Earthsea',
			contributor: 'Lena Hoffmann',
			md5: '4de90bb7215fa3c8e6a1d270',
			olid: 'OL26331930M',
			score: 0.88,
			submittedAt: '2025-01-16'
		},
		{
			id: 'sub_0202',
			title: 'The Lathe of Heaven',
			contributor: 'Lena Hoffmann',
			md5: 'c7f2e8a10d93b45f6e21ab09',
			olid: 'OL32571889M',
			score: 0.91,
			submittedAt: '2025-01-15'
		},
		{
			id: 'sub_0203',
			title: 'Solaris',
			contributor: 'Marek Nowak',
			md5: '8a1f4e2c96db07351bc8d442',
			olid: 'OL7203944M',
			score: 0.96,
			submittedAt: '2025-01-15'
		},
		{
			id: 'sub_0204',
			title: 'Roadside Picnic',
			contributor: 'Marek Nowak',
			md5: 'e39c7b0a54fd12689ea0c317',
			olid: 'OL24721196M',
			score: 0.83,
			submittedAt: '2025-01-14'
		},
		{
			id: 'sub_0205',
			title: 'We',
			contributor: 'Sofia Petrova',
			md5: '2fb6d9e81c4a05372dd1f950',
			olid: 'OL7826547M',
			score: 0.64,
			submittedAt: '2025-01-14'
		},
		{
			id: 'sub_0206',
			title: 'The Master and Margarita',
			contributor: 'Sofia Petrova',
			md5: 'b04e8c2f71a9d3560fe4a128',
			olid: 'OL24357373M',
			score: 0.93,
			submittedAt: '2025-01-13'
		},
		{
			id: 'sub_0207',
			title: 'Invisible Cities',
			contributor: 'Tomas Richter',
			md5: '6d2a9f4b03ce81745ab6e093',
			olid: 'OL4553470M',
			score: 0.89,
			submittedAt: '2025-01-13'
		},
		{
			id: 'sub_0208',
			title: 'If on a Winter’s Night a Traveler',
			contributor: 'Tomas Richter',
			md5: '91c5e7a2d84fb0361cf2d685',
			olid: 'OL4423851M',
			score: 0.77,
			submittedAt: '2025-01-12'
		},
		{
			id: 'sub_0209',
			title: 'The Book of Sand',
			contributor: 'Amara Diallo',
			md5: '5e8b1c9f42ad70638db3e514',
			olid: 'OL7871939M',
			score: 0.95,
			submittedAt: '2025-01-11'
		},
		{
			id: 'sub_0210',
			title: 'Ficciones',
			contributor: 'Amara Diallo',
			md5: '3c7d0a5e18fb92467ea9c206',
			olid: 'OL7828169M',
			score: 0.58,
			submittedAt: '2025-01-11'
		},
		{
			id: 'sub_0211',
			title: 'Pedro Páramo',
			contributor: 'Ines Almeida',
			md5: 'd18f6b3c90ae24751fc7b839',
			olid: 'OL7529846M',
			score: 0.92,
			submittedAt: '2025-01-10'
		},
		{
			id: 'sub_0212',
			title: 'One Hundred Years of Solitude',
			contributor: 'Ines Almeida',
			md5: '7a3e9d1f56cb08243ed5a961',
			olid: 'OL7320293M',
			score: 0.86,
			submittedAt: '2025-01-09'
		}
	];

	const averageScore =
		queue.length > 0
			? queue.reduce((sum, s) => sum + s.score, 0) / queue.length
			: 0;

	const stats: Stat[] = [
		{ label: 'Pending reviews', value: String(queue.length), icon: 'hourglass', accent: 'amber' },
		{ label: 'Avg. validation score', value: averageScore.toFixed(2), icon: 'gauge', accent: 'ink' },
		{ label: 'Oldest pending', value: '7 days', icon: 'calendar-clock', accent: 'neutral' },
		{ label: 'Reviewed today', value: '9', icon: 'check', accent: 'green' }
	];

	const accentStyles: Record<Stat['accent'], string> = {
		amber: 'border-[#F59E0B]/30 bg-[#F59E0B]/10 text-[#B45309]',
		green: 'border-[#22C55E]/30 bg-[#22C55E]/10 text-[#16A34A]',
		ink: 'border-[#8B5CF6]/30 bg-[#8B5CF6]/10 text-[#6D28D9]',
		neutral: 'border-[#E4E4E7] bg-[#F4F4F5] text-[#71717A]'
	};

	function scoreStyle(score: number): string {
		if (score >= 0.9) return 'border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]';
		if (score >= 0.7) return 'border-[#F59E0B]/40 bg-[#F59E0B]/10 text-[#B45309]';
		return 'border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]';
	}

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

{#snippet scoreBadge(score: number)}
	<span
		class="mono inline-flex items-center rounded-full border px-2.5 py-0.5 text-[11px] {scoreStyle(score)}"
	>
		{score.toFixed(2)}
	</span>
{/snippet}

<svelte:head>
	<title>Review Queue — Mond</title>
	<meta
		name="description"
		content="The Mond moderator review queue. Inspect pending mappings and decide what enters the public dataset."
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
						href="/moderator/queue"
						aria-current="page"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#18181B]"
					>
						{@render icon('shield-check', 15)}
						Review queue
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

		<!-- Mobile nav row -->
		<div class="flex items-center gap-1 overflow-x-auto border-t border-[#F4F4F5] px-6 py-2 sm:hidden">
			<a
				href="/dashboard"
				class="flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('layout-dashboard', 14)}
				Dashboard
			</a>
			<a
				href="/moderator/queue"
				aria-current="page"
				class="flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#18181B]"
			>
				{@render icon('shield-check', 14)}
				Review queue
			</a>
			<a
				href="/dataset"
				class="flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('file-down', 14)}
				Dataset
			</a>
		</div>
	</header>

	<main class="morning">
		<div class="mx-auto max-w-6xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ HEADER ============ -->
			<section aria-labelledby="queue-heading">
				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Review queue
				</p>
				<h1
					id="queue-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Pending submissions.
				</h1>
				<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
					Every mapping awaiting human review appears here. Select one to
					inspect and decide whether it should become part of the public
					dataset.
				</p>
			</section>

			<!-- ============ SUMMARY CARDS ============ -->
			<section aria-label="Queue statistics" class="mt-12">
				<dl class="grid grid-cols-2 gap-4 lg:grid-cols-4">
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

			<!-- ============ SEARCH & FILTERS ============ -->
			<section aria-label="Search and filters" class="mt-8">
				<div class="paper rounded-lg p-5 sm:p-6">
					<form class="grid gap-4 lg:grid-cols-[1fr_auto_auto_auto_auto_auto] lg:items-end">
						<div>
							<label
								for="queue-search"
								class="mb-2 block text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]"
							>
								Search
							</label>
							<div class="relative">
								<span
									class="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 text-[#A1A1AA]"
								>
									{@render icon('search', 14)}
								</span>
								<input
									id="queue-search"
									type="search"
									placeholder="Title, MD5, or OLID…"
									class="w-full rounded-md border border-[#E4E4E7] bg-white py-2.5 pl-9 pr-3 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/40 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
								/>
							</div>
						</div>

						<div>
							<label
								for="filter-status"
								class="mb-2 block text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]"
							>
								Status
							</label>
							<select
								id="filter-status"
								class="w-full rounded-md border border-[#E4E4E7] bg-white px-3 py-2.5 text-sm font-light text-[#18181B] focus:border-[#8B5CF6]/40 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10 lg:w-36"
							>
								<option selected>Pending only</option>
								<option>All statuses</option>
							</select>
						</div>

						<div>
							<label
								for="filter-score"
								class="mb-2 block text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]"
							>
								Validation score
							</label>
							<select
								id="filter-score"
								class="w-full rounded-md border border-[#E4E4E7] bg-white px-3 py-2.5 text-sm font-light text-[#18181B] focus:border-[#8B5CF6]/40 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10 lg:w-36"
							>
								<option selected>Highest first</option>
								<option>Lowest first</option>
							</select>
						</div>

						<div>
							<label
								for="filter-date"
								class="mb-2 block text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]"
							>
								Submission date
							</label>
							<select
								id="filter-date"
								class="w-full rounded-md border border-[#E4E4E7] bg-white px-3 py-2.5 text-sm font-light text-[#18181B] focus:border-[#8B5CF6]/40 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10 lg:w-36"
							>
								<option selected>Oldest first</option>
								<option>Newest first</option>
							</select>
						</div>

						<div>
							<label
								for="filter-contributor"
								class="mb-2 block text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]"
							>
								Contributor
							</label>
							<input
								id="filter-contributor"
								type="text"
								placeholder="Any"
								class="w-full rounded-md border border-[#E4E4E7] bg-white px-3 py-2.5 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/40 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10 lg:w-36"
							/>
						</div>

						<div>
							<button
								type="button"
								class="flex w-full items-center justify-center gap-2 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-5 py-2.5 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14] lg:w-auto"
							>
								{@render icon('filter', 13)}
								Filter
							</button>
						</div>
					</form>
				</div>
			</section>

			<!-- ============ PENDING REVIEW TABLE ============ -->
			<section aria-labelledby="pending-heading" class="mt-16">
				<div class="mb-6">
					<p class="mb-2 text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]">
						— Awaiting review —
					</p>
					<h2 id="pending-heading" class="text-xl font-extralight tracking-tight text-[#18181B]">
						{queue.length} mappings in the queue
					</h2>
				</div>

				{#if queue.length === 0}
					<!-- Empty state -->
					<div class="paper rounded-lg px-8 py-20 text-center">
						<div class="mx-auto mb-6 flex justify-center">
							<span class="phase-crescent" aria-hidden="true"></span>
						</div>
						<h3 class="text-lg font-extralight tracking-tight text-[#18181B]">
							Nothing waiting for review.
						</h3>
						<p class="quote mx-auto mt-3 max-w-sm text-[15px] leading-relaxed text-[#71717A]">
							Every submitted mapping has been processed.
						</p>
						<div class="mt-8">
							<a
								href="/dashboard"
								class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
							>
								{@render icon('layout-dashboard', 15)}
								Return to dashboard
							</a>
						</div>
					</div>
				{:else}
					<!-- Desktop: table -->
					<div class="paper hidden overflow-hidden rounded-lg md:block">
						<table class="w-full text-left">
							<caption class="sr-only">
								Pending mapping submissions awaiting moderator review
							</caption>
							<thead>
								<tr class="border-b border-[#F4F4F5]">
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Book title
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Contributor
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
										Submitted
									</th>
									<th scope="col" class="px-6 py-4 text-right text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Action
									</th>
								</tr>
							</thead>
							<tbody>
								{#each queue as submission (submission.id)}
									<tr class="border-b border-[#F4F4F5] transition-colors last:border-0 hover:bg-[#FAFAFA]">
										<td class="px-6 py-4">
											<span class="block text-sm font-light text-[#18181B]">
												{submission.title}
											</span>
											<span class="mono mt-0.5 block text-xs text-[#A1A1AA]">
												{submission.id}
											</span>
										</td>
										<td class="px-6 py-4">
											<span class="text-sm font-light text-[#52525B]">
												{submission.contributor}
											</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#3F3F46]" title={submission.md5}>
												{truncateMd5(submission.md5)}
											</span>
										</td>
										<td class="px-6 py-4">
											<span class="mono text-sm text-[#6366F1]">{submission.olid}</span>
										</td>
										<td class="px-6 py-4">
											{@render scoreBadge(submission.score)}
										</td>
										<td class="px-6 py-4">
											<time
												datetime={submission.submittedAt}
												class="text-sm font-light text-[#71717A]"
											>
												{formatDate(submission.submittedAt)}
											</time>
										</td>
										<td class="px-6 py-4 text-right">
											<a
												href="/moderator/review/{submission.id}"
												class="inline-flex items-center gap-1.5 rounded-md border border-[#E4E4E7] bg-white px-3.5 py-1.5 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
											>
												Review
												{@render icon('arrow-up-right', 12)}
											</a>
										</td>
									</tr>
								{/each}
							</tbody>
						</table>
					</div>

					<!-- Mobile: stacked cards -->
					<ul class="space-y-4 md:hidden">
						{#each queue as submission (submission.id)}
							<li class="paper rounded-lg p-5">
								<div class="flex items-start justify-between gap-4">
									<div>
										<p class="text-sm font-light text-[#18181B]">{submission.title}</p>
										<p class="mt-1 text-xs font-light text-[#71717A]">
											{submission.contributor}
										</p>
									</div>
									{@render scoreBadge(submission.score)}
								</div>
								<dl class="mt-4 grid grid-cols-3 gap-3 border-t border-[#F4F4F5] pt-4">
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">MD5</dt>
										<dd class="mono mt-1 text-xs text-[#3F3F46]" title={submission.md5}>
											{truncateMd5(submission.md5)}
										</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">OLID</dt>
										<dd class="mono mt-1 text-xs text-[#6366F1]">{submission.olid}</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Submitted</dt>
										<dd class="mt-1 text-xs font-light text-[#71717A]">
											<time datetime={submission.submittedAt}>{formatDate(submission.submittedAt)}</time>
										</dd>
									</div>
								</dl>
								<div class="mt-4">
									<a
										href="/moderator/review/{submission.id}"
										class="flex w-full items-center justify-center gap-1.5 rounded-md border border-[#E4E4E7] bg-white px-4 py-2.5 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
									>
										Review
										{@render icon('arrow-up-right', 12)}
									</a>
								</div>
							</li>
						{/each}
					</ul>
				{/if}
			</section>

			<!-- ============ QUEUE INFORMATION ============ -->
			{#if queue.length > 0}
				<section aria-labelledby="notes-heading" class="mt-8">
					<div class="paper rounded-lg p-6 sm:p-8">
						<div class="flex items-start gap-4">
							<span
								class="flex h-9 w-9 shrink-0 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/10 text-[#6D28D9]"
							>
								{@render icon('shield-check', 15)}
							</span>
							<div>
								<h2
									id="notes-heading"
									class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
								>
									Moderation notes
								</h2>
								<p class="mt-2 text-sm font-light leading-relaxed text-[#52525B]">
									Submissions are reviewed in chronological order unless urgent
									corrections require priority handling.
								</p>
							</div>
						</div>
					</div>
				</section>
			{/if}

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light text-[#A1A1AA]">
				Every decision you make here is recorded. The dataset carries its own provenance.
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