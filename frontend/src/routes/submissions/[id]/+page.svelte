svelte
<!-- src/routes/submissions/[id]/+page.svelte -->
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
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'arrow-left': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>',
		'arrow-down': '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
		library: '<path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/>',
		'search-check':
			'<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		'shield-check':
			'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
		upload:
			'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>',
		stamp:
			'<path d="M5 22h14"/><path d="M19.27 13.73A2.5 2.5 0 0 0 17.5 13h-11A2.5 2.5 0 0 0 4 15.5V17a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-1.5c0-.66-.26-1.3-.73-1.77Z"/><path d="M14 13V8.5C14 7 15 7 15 5a3 3 0 0 0-6 0c0 2 1 2 1 3.5V13"/>',
		hash: '<line x1="4" x2="20" y1="9" y2="9"/><line x1="4" x2="20" y1="15" y2="15"/><line x1="10" x2="8" y1="3" y2="21"/><line x1="16" x2="14" y1="3" y2="21"/>'
	};

	type SubmissionStatus = 'pending' | 'approved' | 'rejected';

	// Mock record. Replace with load() data in production.
	const contributor = {
		name: 'Lena Hoffmann',
		email: 'lena@posteo.de',
		initials: 'LH'
	};

	const record = {
		id: 'sub_0197',
		title: 'The Left Hand of Darkness',
		status: 'approved' as SubmissionStatus,
		confidence: 0.97,
		submittedAt: '2025-01-18T09:42:00Z',
		validatedAt: '2025-01-18T09:42:07Z',
		reviewedAt: '2025-01-21T14:16:00Z',
		approvedAt: '2025-01-21T14:16:00Z',
		reviewer: 'Moderator #14',
		comment:
			'Edition matches the original Ace Books printing. Metadata aligns with Open Library. ISBN verified manually.',
		validationVersion: 'v2.4.1',
		createdAt: '2025-01-18T09:42:00Z',
		updatedAt: '2025-01-21T14:16:00Z',
		source: 'annas-archive',
		editionId: 'OL7602281M',
		md5: 'f2b4d1a9c07e83aa41c69e12'
	};

	type ComparisonRow = {
		field: string;
		anna: string;
		openLibrary: string;
		match: boolean;
		mono?: boolean;
	};

	const comparison: ComparisonRow[] = [
		{
			field: 'Title',
			anna: 'The Left Hand of Darkness',
			openLibrary: 'The Left Hand of Darkness',
			match: true
		},
		{ field: 'Author', anna: 'Ursula K. Le Guin', openLibrary: 'Ursula K. Le Guin', match: true },
		{ field: 'Publisher', anna: 'Ace Books', openLibrary: 'Ace Books', match: true },
		{ field: 'Language', anna: 'English', openLibrary: 'English', match: true },
		{ field: 'Year', anna: '1969', openLibrary: '1969', match: true },
		{
			field: 'ISBN',
			anna: '978-0-441-47812-5',
			openLibrary: '978-0-441-47812-5',
			match: true,
			mono: true
		}
	];

	const validationChecks: string[] = [
		'Title matched',
		'Author matched',
		'ISBN checksum valid',
		'Publisher matched',
		'Publication year matched',
		'Language matched'
	];

	type TimelineStep = {
		icon: string;
		title: string;
		desc: string;
		timestamp: string; // ISO
	};

	const timeline: TimelineStep[] = [
		{
			icon: 'upload',
			title: 'Submitted',
			desc: 'Mapping proposed by the contributor and entered into the review queue.',
			timestamp: record.submittedAt
		},
		{
			icon: 'search-check',
			title: 'Automatic validation completed',
			desc: 'Six of six checks passed. Confidence score computed at 0.97.',
			timestamp: record.validatedAt
		},
		{
			icon: 'shield-check',
			title: 'Moderator reviewed',
			desc: 'Read in full by a community moderator. Edition confirmed manually.',
			timestamp: record.reviewedAt
		},
		{
			icon: 'stamp',
			title: 'Approved',
			desc: 'Entered into the public dataset. Permanent, attributed, and free.',
			timestamp: record.approvedAt
		}
	];

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

	function formatDate(iso: string): string {
		return new Date(iso).toLocaleDateString('en-GB', {
			day: 'numeric',
			month: 'long',
			year: 'numeric'
		});
	}

	function formatDateTime(iso: string): string {
		const d = new Date(iso);
		return (
			d.toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric' }) +
			' · ' +
			d.toLocaleTimeString('en-GB', { hour: '2-digit', minute: '2-digit', timeZone: 'UTC' }) +
			' UTC'
		);
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
	<title>{record.title} — Submission Record — Mond</title>
	<meta
		name="description"
		content="A permanent archival record of a verified mapping between Anna’s Archive and Open Library."
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
		<div class="mx-auto max-w-3xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ BREADCRUMB ============ -->
			<a
				href="/submissions"
				class="inline-flex items-center gap-2 text-sm font-light text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('arrow-left', 14)}
				All submissions
			</a>

			<!-- ============ HERO ============ -->
			<section aria-labelledby="record-heading" class="mt-12 text-center">
				<p class="mb-4 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					— Submission record —
				</p>
				<h1
					id="record-heading"
					class="text-balance text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					{record.title}
				</h1>
				<p class="mx-auto mt-5 max-w-md text-sm font-light leading-relaxed text-[#52525B]">
					A permanent record of this contribution, including validation results
					and moderator review.
				</p>
				<p class="mono mt-6 text-xs text-[#A1A1AA]">{record.id}</p>
			</section>

			<!-- ============ STATUS ============ -->
			<section aria-label="Record status" class="mt-14">
				<div class="paper sealed rounded-lg p-6 sm:p-8">
					<dl class="grid grid-cols-2 gap-x-6 gap-y-8 sm:grid-cols-5">
						<div>
							<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">Status</dt>
							<dd class="mt-3">{@render statusBadge(record.status)}</dd>
						</div>
						<div>
							<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">Confidence</dt>
							<dd class="mono mt-3 text-sm text-[#18181B]">
								{Math.round(record.confidence * 100)}%
							</dd>
						</div>
						<div>
							<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">Submitted</dt>
							<dd class="mt-3 text-sm font-light text-[#3F3F46]">
								<time datetime={record.submittedAt}>{formatDate(record.submittedAt)}</time>
							</dd>
						</div>
						<div>
							<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">Reviewed</dt>
							<dd class="mt-3 text-sm font-light text-[#3F3F46]">
								<time datetime={record.reviewedAt}>{formatDate(record.reviewedAt)}</time>
							</dd>
						</div>
						<div>
							<dt class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">Reviewer</dt>
							<dd class="mono mt-3 text-sm text-[#6D28D9]">{record.reviewer}</dd>
						</div>
					</dl>
				</div>
			</section>

			<!-- ============ CENTERPIECE: METADATA COMPARISON ============ -->
			<section aria-labelledby="comparison-heading" class="mt-24">
				<p class="mb-4 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					— The comparison —
				</p>
				<h2
					id="comparison-heading"
					class="text-balance text-center text-2xl font-extralight tracking-tight text-[#18181B] sm:text-3xl"
				>
					Two records, side by side.
				</h2>
				<p class="mx-auto mt-4 max-w-md text-center text-sm font-light leading-relaxed text-[#52525B]">
					The evidence on which this mapping rests. Matching fields are
					marked in green.
				</p>

				<div class="paper mt-12 overflow-hidden rounded-lg">
					<!-- Column headers -->
					<div class="grid grid-cols-2 border-b border-[#F4F4F5]">
						<div class="flex items-center gap-2 border-r border-[#F4F4F5] px-6 py-5 sm:px-8">
							<span class="text-[#71717A]">{@render icon('book-marked', 13)}</span>
							<span class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
								Anna’s Archive
							</span>
							<span class="mono ml-auto hidden text-[11px] text-[#A1A1AA] sm:inline">source</span>
						</div>
						<div class="flex items-center gap-2 px-6 py-5 sm:px-8">
							<span class="text-[#71717A]">{@render icon('library', 13)}</span>
							<span class="text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
								Open Library
							</span>
							<span class="mono ml-auto hidden text-[11px] text-[#A1A1AA] sm:inline">target</span>
						</div>
					</div>

					<!-- Field rows -->
					{#each comparison as row (row.field)}
						<div class="grid grid-cols-2 border-b border-[#F4F4F5]">
							<div class="border-r border-[#F4F4F5] px-6 py-4 sm:px-8">
								<p class="flex items-center gap-1.5 text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">
									{row.field}
								</p>
								<p
									class="mt-1.5 text-sm font-light {row.mono ? 'mono' : ''} {row.match
										? 'text-[#16A34A]'
										: 'text-[#3F3F46]'}"
								>
									{row.anna}
								</p>
							</div>
							<div class="px-6 py-4 sm:px-8">
								<p class="flex items-center justify-between gap-1.5 text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">
									{row.field}
									{#if row.match}
										<span
											class="flex h-3.5 w-3.5 items-center justify-center rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]"
											title="Fields match"
										>
											{@render icon('check', 8, 2.5)}
										</span>
										<span class="sr-only">— matched</span>
									{/if}
								</p>
								<p
									class="mt-1.5 text-sm font-light {row.mono ? 'mono' : ''} {row.match
										? 'text-[#16A34A]'
										: 'text-[#3F3F46]'}"
								>
									{row.openLibrary}
								</p>
							</div>
						</div>
					{/each}

					<!-- Identifier row -->
					<div class="grid grid-cols-2">
						<div class="border-r border-[#F4F4F5] bg-[#FAFAFA] px-6 py-4 sm:px-8">
							<p class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">MD5</p>
							<p class="mono mt-1.5 break-all text-sm text-[#3F3F46]" title={record.md5}>
								{record.md5.slice(0, 8)}…{record.md5.slice(-4)}
							</p>
						</div>
						<div class="bg-[#FAFAFA] px-6 py-4 sm:px-8">
							<p class="text-[10px] tracking-[0.2em] uppercase text-[#A1A1AA]">OLID</p>
							<p class="mono mt-1.5 text-sm text-[#6366F1]">{record.editionId}</p>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ VALIDATION SUMMARY ============ -->
			<section aria-labelledby="validation-heading" class="mt-16">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6">
						<span
							id="validation-heading"
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							{@render icon('search-check', 13)}
							Validation summary
						</span>
					</div>

					<div class="grid gap-10 sm:grid-cols-[1fr_auto] sm:items-center">
						<ul class="space-y-3">
							{#each validationChecks as check}
								<li class="flex items-center gap-3 text-sm font-light text-[#3F3F46]">
									<span
										class="flex h-4 w-4 items-center justify-center rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]"
									>
										{@render icon('check', 9, 2.5)}
									</span>
									{check}
								</li>
							{/each}
						</ul>

						<div class="border-t border-[#F4F4F5] pt-8 text-center sm:border-l sm:border-t-0 sm:pl-12 sm:pt-0">
							<p class="mono text-5xl font-light text-[#6366F1]">
								{Math.round(record.confidence * 100)}<span class="text-2xl text-[#A1A1AA]">%</span>
							</p>
							<p class="mt-3 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
								High confidence match
							</p>
							<p class="mono mt-2 text-xs text-[#A1A1AA]">6 of 6 checks passed</p>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ MODERATOR REVIEW ============ -->
			<section aria-labelledby="review-heading" class="mt-16">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6 flex items-center justify-between">
						<span
							id="review-heading"
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							{@render icon('shield-check', 13)}
							Moderator decision
						</span>
						{@render statusBadge(record.status)}
					</div>

					<blockquote class="quote text-[17px] leading-relaxed text-[#3F3F46]">
						“{record.comment}”
					</blockquote>

					<div class="mt-6 flex flex-wrap items-center gap-x-6 gap-y-2 border-t border-[#F4F4F5] pt-5">
						<p class="mono text-xs text-[#A1A1AA]">
							reviewed by <span class="text-[#6D28D9]">{record.reviewer}</span>
						</p>
						<p class="text-xs font-light text-[#A1A1AA]">
							<time datetime={record.reviewedAt}>{formatDate(record.reviewedAt)}</time>
						</p>
					</div>
				</div>
			</section>

			<!-- ============ TIMELINE ============ -->
			<section aria-labelledby="timeline-heading" class="mt-24">
				<p class="mb-4 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					— The journey —
				</p>
				<h2
					id="timeline-heading"
					class="text-balance text-center text-2xl font-extralight tracking-tight text-[#18181B] sm:text-3xl"
				>
					From submission to seal.
				</h2>

				<div class="relative mx-auto mt-14 max-w-lg">
					<!-- ink thread -->
					<div
						class="thread pointer-events-none absolute left-[21px] top-0 h-full w-px"
						aria-hidden="true"
					></div>

					<ol class="space-y-10">
						{#each timeline as step, i (step.title)}
							<li class="relative flex gap-6">
								<div
									class="relative z-10 flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-[#E4E4E7] bg-white text-[#6366F1] shadow-sm"
								>
									{@render icon(step.icon, 16)}
								</div>
								<div class="pt-0.5">
									<p class="mono mb-1 text-[11px] text-[#A1A1AA]">0{i + 1}</p>
									<h3 class="text-base font-medium text-[#18181B]">{step.title}</h3>
									<p class="mt-1.5 text-sm font-light leading-relaxed text-[#52525B]">
										{step.desc}
									</p>
									<p class="mono mt-2 text-xs text-[#A1A1AA]">
										<time datetime={step.timestamp}>{formatDateTime(step.timestamp)}</time>
									</p>
								</div>
							</li>
						{/each}
					</ol>
				</div>
			</section>

			<!-- ============ TECHNICAL METADATA ============ -->
			<section aria-labelledby="technical-heading" class="mt-24">
				<div class="paper mx-auto max-w-lg rounded-lg p-6 sm:p-7">
					<div class="mb-5">
						<span
							id="technical-heading"
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							{@render icon('hash', 13)}
							Technical metadata
						</span>
					</div>
					<dl class="mono space-y-2.5 text-xs">
						<div class="flex items-baseline justify-between gap-4">
							<dt class="text-[#A1A1AA]">submission_id</dt>
							<dd class="text-[#3F3F46]">{record.id}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-4">
							<dt class="text-[#A1A1AA]">created_at</dt>
							<dd class="text-[#3F3F46]">{record.createdAt}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-4">
							<dt class="text-[#A1A1AA]">updated_at</dt>
							<dd class="text-[#3F3F46]">{record.updatedAt}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-4">
							<dt class="text-[#A1A1AA]">validation_version</dt>
							<dd class="text-[#3F3F46]">{record.validationVersion}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-4">
							<dt class="text-[#A1A1AA]">source</dt>
							<dd class="text-[#3F3F46]">{record.source}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-4">
							<dt class="text-[#A1A1AA]">edition_id</dt>
							<dd class="text-[#6366F1]">{record.editionId}</dd>
						</div>
					</dl>
				</div>
			</section>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<div class="mt-24 text-center">
				<div class="mb-6 flex justify-center">
					<span class="phase-full" aria-hidden="true"></span>
				</div>
				<p class="quote mx-auto max-w-sm text-[15px] leading-relaxed text-[#71717A]">
					“Every approved mapping becomes a permanent part of Mond’s public dataset.”
				</p>
			</div>
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

	/* ---- Ink thread (timeline) ---- */
	.thread {
		background: linear-gradient(
			to bottom,
			transparent,
			rgba(99, 102, 241, 0.3) 12%,
			rgba(99, 102, 241, 0.3) 88%,
			transparent
		);
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

	.phase-full {
		display: inline-block;
		height: 32px;
		width: 32px;
		border-radius: 9999px;
		background: #6366f1;
		box-shadow: 0 4px 16px -4px rgba(99, 102, 241, 0.45);
	}
</style>