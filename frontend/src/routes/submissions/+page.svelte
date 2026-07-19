svelte
<!-- src/routes/submissions/+page.svelte -->
<script lang="ts">
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
		percent:
			'<line x1="19" x2="5" y1="5" y2="19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		upload:
			'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>',
		'arrow-up-right': '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>'
	};

	const contributor = {
		name: 'Lena Hoffmann',
		email: 'lena@posteo.de',
		initials: 'LH'
	};

	type SubmissionStatus = 'pending' | 'approved' | 'rejected';

	type Submission = {
		id: string;
		md5: string;
		olid: string;
		title: string;
		author: string;
		score: number;
		status: SubmissionStatus;
		submittedAt: string; // ISO date
	};

	// Realistic mock data. Replace with load() data in production.
	const submissions: Submission[] = [
		{
			id: 'sub_0197',
			md5: 'f2b4d1a9c07e83aa41c69e12',
			olid: 'OL7602281M',
			title: 'The Left Hand of Darkness',
			author: 'Ursula K. Le Guin',
			score: 0.97,
			status: 'approved',
			submittedAt: '2025-01-18'
		},
		{
			id: 'sub_0196',
			md5: 'a81c3f5d92be04711fd08c44',
			olid: 'OL24347578M',
			title: 'The Dispossessed',
			author: 'Ursula K. Le Guin',
			score: 0.94,
			status: 'approved',
			submittedAt: '2025-01-17'
		},
		{
			id: 'sub_0195',
			md5: '4de90bb7215fa3c8e6a1d270',
			olid: 'OL26331930M',
			title: 'A Wizard of Earthsea',
			author: 'Ursula K. Le Guin',
			score: 0.88,
			status: 'pending',
			submittedAt: '2025-01-16'
		},
		{
			id: 'sub_0194',
			md5: 'c7f2e8a10d93b45f6e21ab09',
			olid: 'OL32571889M',
			title: 'The Lathe of Heaven',
			author: 'Ursula K. Le Guin',
			score: 0.91,
			status: 'pending',
			submittedAt: '2025-01-15'
		},
		{
			id: 'sub_0193',
			md5: '9b0e4c6d3f1a82750cd4e918',
			olid: 'OL3168483M',
			title: 'Always Coming Home',
			author: 'Ursula K. Le Guin',
			score: 0.62,
			status: 'rejected',
			submittedAt: '2025-01-12'
		},
		{
			id: 'sub_0192',
			md5: '17d5a2c94eb60f38a2b7c501',
			olid: 'OL7827093M',
			title: 'The Word for World Is Forest',
			author: 'Ursula K. Le Guin',
			score: 0.95,
			status: 'approved',
			submittedAt: '2025-01-10'
		},
		{
			id: 'sub_0191',
			md5: '6ea1f80cb3274d95e0182fc3',
			olid: 'OL7353617M',
			title: 'Fahrenheit 451',
			author: 'Ray Bradbury',
			score: 0.93,
			status: 'approved',
			submittedAt: '2025-01-07'
		},
		{
			id: 'sub_0190',
			md5: 'd30c7b9f14a2e6580cb1d947',
			olid: 'OL24721971M',
			title: 'The Martian Chronicles',
			author: 'Ray Bradbury',
			score: 0.84,
			status: 'pending',
			submittedAt: '2025-01-04'
		},
		{
			id: 'sub_0189',
			md5: '2f8ba6d05c917e43ad60b28e',
			olid: 'OL26885115M',
			title: 'Solaris',
			author: 'Stanisław Lem',
			score: 0.71,
			status: 'rejected',
			submittedAt: '2025-01-02'
		},
		{
			id: 'sub_0188',
			md5: 'b49e2c7a80d5f316c2e94a07',
			olid: 'OL7826547M',
			title: 'Roadside Picnic',
			author: 'Arkady & Boris Strugatsky',
			score: 0.89,
			status: 'approved',
			submittedAt: '2024-12-29'
		},
		{
			id: 'sub_0187',
			md5: 'e05d3a81f6c94b27a10de853',
			olid: 'OL32066235M',
			title: 'We',
			author: 'Yevgeny Zamyatin',
			score: 0.78,
			status: 'pending',
			submittedAt: '2024-12-24'
		},
		{
			id: 'sub_0186',
			md5: '73c1e9f4ab08d2657f40b19c',
			olid: 'OL7360837M',
			title: 'The Book of the New Sun',
			author: 'Gene Wolfe',
			score: 0.99,
			status: 'approved',
			submittedAt: '2024-12-20'
		}
	];

	const counts = {
		pending: submissions.filter((s) => s.status === 'pending').length,
		approved: submissions.filter((s) => s.status === 'approved').length,
		rejected: submissions.filter((s) => s.status === 'rejected').length
	};

	const decided = counts.approved + counts.rejected;
	const acceptanceRate = decided > 0 ? Math.round((counts.approved / decided) * 100) : 0;

	type Stat = {
		label: string;
		value: string;
		icon: string;
		accent: 'amber' | 'green' | 'red' | 'ink';
	};

	const stats: Stat[] = [
		{ label: 'Pending', value: String(counts.pending), icon: 'hourglass', accent: 'amber' },
		{ label: 'Approved', value: String(counts.approved), icon: 'check', accent: 'green' },
		{ label: 'Rejected', value: String(counts.rejected), icon: 'x', accent: 'red' },
		{ label: 'Acceptance rate', value: `${acceptanceRate}%`, icon: 'percent', accent: 'ink' }
	];

	const accentStyles: Record<Stat['accent'], string> = {
		amber: 'border-[#F59E0B]/30 bg-[#F59E0B]/10 text-[#B45309]',
		green: 'border-[#22C55E]/30 bg-[#22C55E]/10 text-[#16A34A]',
		red: 'border-[#EF4444]/30 bg-[#EF4444]/10 text-[#DC2626]',
		ink: 'border-[#8B5CF6]/30 bg-[#8B5CF6]/10 text-[#6D28D9]'
	};

	const statusStyles: Record<SubmissionStatus, string> = {
		approved: 'border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]',
		pending: 'border-[#F59E0B]/40 bg-[#F59E0B]/10 text-[#B45309]',
		rejected: 'border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]'
	};

	const statusLabels: Record<SubmissionStatus, string> = {
		approved: 'Approved',
		pending: 'Pending',
		rejected: 'Rejected'
	};

	// ---- Filtering & sorting (client-side, mock) ----
	type StatusFilter = 'all' | SubmissionStatus;
	type SortOrder = 'newest' | 'oldest' | 'highest' | 'lowest';

	let query = $state('');
	let statusFilter = $state<StatusFilter>('all');
	let sortOrder = $state<SortOrder>('newest');

	const filtered = $derived.by(() => {
		const q = query.trim().toLowerCase();

		let list = submissions.filter((s) => {
			const matchesStatus = statusFilter === 'all' || s.status === statusFilter;
			const matchesQuery =
				q === '' ||
				s.title.toLowerCase().includes(q) ||
				s.author.toLowerCase().includes(q) ||
				s.md5.toLowerCase().includes(q) ||
				s.olid.toLowerCase().includes(q);
			return matchesStatus && matchesQuery;
		});

		return [...list].sort((a, b) => {
			switch (sortOrder) {
				case 'newest':
					return b.submittedAt.localeCompare(a.submittedAt);
				case 'oldest':
					return a.submittedAt.localeCompare(b.submittedAt);
				case 'highest':
					return b.score - a.score;
				case 'lowest':
					return a.score - b.score;
			}
		});
	});

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

	function formatScore(score: number): string {
		return `${Math.round(score * 100)}%`;
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

{#snippet statusBadge(status: SubmissionStatus)}
	<span
		class="inline-flex items-center gap-1.5 rounded-full border px-2.5 py-0.5 text-[11px] {statusStyles[status]}"
	>
		{statusLabels[status]}
	</span>
{/snippet}

<svelte:head>
	<title>Your submissions — Mond</title>
	<meta
		name="description"
		content="Every mapping you’ve contributed to Mond. Track validation results and moderation decisions."
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
					aria-label="Account menu for {contributor.name}"
				>
					<span
						class="flex h-8 w-8 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] text-xs font-medium text-[#6D28D9]"
					>
						{contributor.initials}
					</span>
					<span class="hidden text-sm font-light text-[#3F3F46] sm:inline">{contributor.name}</span>
					<span class="text-[#A1A1AA]">{@render icon('chevron-down', 14)}</span>
				</summary>

				<div
					class="paper absolute right-0 z-30 mt-2 w-56 overflow-hidden rounded-lg py-1.5"
					role="menu"
				>
					<div class="border-b border-[#F4F4F5] px-4 py-3">
						<p class="text-sm text-[#18181B]">{contributor.name}</p>
						<p class="mono mt-0.5 text-xs text-[#A1A1AA]">{contributor.email}</p>
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
		<div class="mx-auto max-w-6xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ HERO ============ -->
			<section aria-labelledby="submissions-heading">
				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Contributor record
				</p>
				<h1
					id="submissions-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Your submissions.
				</h1>
				<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
					Every mapping you’ve contributed to Mond. Track validation results
					and moderation decisions.
				</p>
			</section>

			<!-- ============ STATISTICS ============ -->
			<section aria-label="Submission statistics" class="mt-12">
				<dl class="grid grid-cols-2 gap-4 lg:grid-cols-4">
					{#each stats as stat}
						<div class="paper rounded-lg p-5 sm:p-6">
							<div class="flex items-center justify-between">
								<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
									{stat.label}
								</dt>
								<span
									class="flex h-7 w-7 items-center justify-center rounded-full border {accentStyles[stat.accent]}"
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

			<!-- ============ FILTER BAR ============ -->
			<section aria-label="Filter submissions" class="mt-10">
				<div class="paper rounded-lg p-4 sm:p-5">
					<div class="flex flex-col gap-3 sm:flex-row sm:items-center">
						<!-- Search -->
						<div class="relative flex-1">
							<span class="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 text-[#A1A1AA]">
								{@render icon('search', 14)}
							</span>
							<label for="search" class="sr-only">Search submissions</label>
							<input
								id="search"
								type="search"
								bind:value={query}
								placeholder="Search by title, MD5 or OLID"
								autocomplete="off"
								spellcheck="false"
								class="w-full rounded-md border border-[#E4E4E7] bg-white py-2.5 pl-10 pr-4 text-sm font-light text-[#18181B] shadow-sm transition-colors placeholder:text-[#A1A1AA] focus:border-[#8B5CF6]/50 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
							/>
						</div>

						<!-- Status filter -->
						<div class="relative sm:w-40">
							<label for="status-filter" class="sr-only">Filter by status</label>
							<select
								id="status-filter"
								bind:value={statusFilter}
								class="w-full appearance-none rounded-md border border-[#E4E4E7] bg-white py-2.5 pl-4 pr-9 text-sm font-light text-[#3F3F46] shadow-sm transition-colors focus:border-[#8B5CF6]/50 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
							>
								<option value="all">All</option>
								<option value="pending">Pending</option>
								<option value="approved">Approved</option>
								<option value="rejected">Rejected</option>
							</select>
							<span class="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[#A1A1AA]">
								{@render icon('chevron-down', 14)}
							</span>
						</div>

						<!-- Sort order -->
						<div class="relative sm:w-44">
							<label for="sort-order" class="sr-only">Sort order</label>
							<select
								id="sort-order"
								bind:value={sortOrder}
								class="w-full appearance-none rounded-md border border-[#E4E4E7] bg-white py-2.5 pl-4 pr-9 text-sm font-light text-[#3F3F46] shadow-sm transition-colors focus:border-[#8B5CF6]/50 focus:outline-none focus:ring-2 focus:ring-[#8B5CF6]/10"
							>
								<option value="newest">Newest first</option>
								<option value="oldest">Oldest first</option>
								<option value="highest">Highest score</option>
								<option value="lowest">Lowest score</option>
							</select>
							<span class="pointer-events-none absolute right-3 top-1/2 -translate-y-1/2 text-[#A1A1AA]">
								{@render icon('chevron-down', 14)}
							</span>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ SUBMISSIONS ============ -->
			<section aria-label="Submission list" class="mt-6">
				<!-- Result count -->
				<p class="mb-4 px-1 text-xs font-light text-[#A1A1AA]" aria-live="polite">
					{filtered.length}
					{filtered.length === 1 ? 'record' : 'records'}
				</p>

				{#if filtered.length === 0}
					<!-- Empty state -->
					<div class="paper rounded-lg px-8 py-20 text-center">
						<div class="mx-auto mb-6 flex justify-center">
							<span class="phase-crescent" aria-hidden="true"></span>
						</div>
						<h2 class="text-lg font-extralight tracking-tight text-[#18181B]">
							No submissions yet.
						</h2>
						<p class="quote mx-auto mt-3 max-w-sm text-[15px] leading-relaxed text-[#71717A]">
							“Every archive begins with a single record.”
						</p>
						<div class="mt-8">
							<a
								href="/submit"
								class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
							>
								{@render icon('upload', 15)}
								Submit your first mapping
							</a>
						</div>
					</div>
				{:else}
					<!-- Desktop: table -->
					<div class="paper hidden overflow-hidden rounded-lg lg:block">
						<table class="w-full text-left">
							<caption class="sr-only">
								Your mapping submissions with confidence scores, status, and submission dates
							</caption>
							<thead>
								<tr class="border-b border-[#F4F4F5]">
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Book
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										MD5
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Open Library ID
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Confidence
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Status
									</th>
									<th scope="col" class="px-6 py-4 text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										Submitted
									</th>
									<th scope="col" class="px-6 py-4 text-right text-[11px] font-normal tracking-[0.25em] uppercase text-[#A1A1AA]">
										<span class="sr-only">Action</span>
									</th>
								</tr>
							</thead>
							<tbody>
								{#each filtered as submission (submission.id)}
									<tr class="border-b border-[#F4F4F5] transition-colors last:border-0 hover:bg-[#FAFAFA]">
										<td class="px-6 py-4">
											<span class="block text-sm font-light text-[#18181B]">
												{submission.title}
											</span>
											<span class="mt-0.5 block text-xs font-light text-[#A1A1AA]">
												{submission.author}
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
											<span class="mono text-sm text-[#3F3F46]">
												{formatScore(submission.score)}
											</span>
										</td>
										<td class="px-6 py-4">
											{@render statusBadge(submission.status)}
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
												href="/submissions/{submission.id}"
												class="inline-flex items-center gap-1.5 rounded-md border border-[#E4E4E7] bg-white px-3 py-1.5 text-xs text-[#71717A] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05] hover:text-[#18181B]"
												aria-label="View submission for {submission.title}"
											>
												View
												{@render icon('arrow-up-right', 11)}
											</a>
										</td>
									</tr>
								{/each}
							</tbody>
						</table>
					</div>

					<!-- Mobile & tablet: stacked cards -->
					<ul class="space-y-4 lg:hidden">
						{#each filtered as submission (submission.id)}
							<li class="paper rounded-lg p-5">
								<div class="flex items-start justify-between gap-4">
									<div>
										<p class="text-sm font-light text-[#18181B]">{submission.title}</p>
										<p class="mt-0.5 text-xs font-light text-[#A1A1AA]">{submission.author}</p>
									</div>
									{@render statusBadge(submission.status)}
								</div>

								<dl class="mt-4 grid grid-cols-2 gap-x-4 gap-y-3 border-t border-[#F4F4F5] pt-4">
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
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Confidence</dt>
										<dd class="mono mt-1 text-xs text-[#3F3F46]">{formatScore(submission.score)}</dd>
									</div>
									<div>
										<dt class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">Submitted</dt>
										<dd class="mt-1 text-xs font-light text-[#71717A]">
											<time datetime={submission.submittedAt}>{formatDate(submission.submittedAt)}</time>
										</dd>
									</div>
								</dl>

								<div class="mt-4 border-t border-[#F4F4F5] pt-4">
									<a
										href="/submissions/{submission.id}"
										class="flex w-full items-center justify-center gap-1.5 rounded-md border border-[#E4E4E7] bg-white px-4 py-2 text-xs text-[#71717A] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05] hover:text-[#18181B]"
										aria-label="View submission for {submission.title}"
									>
										View
										{@render icon('arrow-up-right', 11)}
									</a>
								</div>
							</li>
						{/each}
					</ul>
				{/if}
			</section>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light text-[#A1A1AA]">
				Every approved mapping becomes part of Mond’s permanent public dataset.
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