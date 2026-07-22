<script lang="ts">
	import { goto } from "$app/navigation";
	import { user } from "$lib/stores/auth";

	$effect(() => {
	if (!$user) {
		goto("/login");
		return;
	}

	if (
		$user.role !== "moderator" &&
		$user.role !== "admin"
	) {
		goto("/dashboard");
	}
	});

	
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
		x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
		hourglass:
			'<path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.172a2 2 0 0 0-.586-1.414L12 12l-4.414 4.414A2 2 0 0 0 7 17.828V22"/><path d="M7 2v4.172a2 2 0 0 0 .586 1.414L12 12l4.414-4.414A2 2 0 0 0 17 6.172V2"/>',
		gauge: '<path d="m12 14 4-4"/><path d="M3.34 19a10 10 0 1 1 17.32 0"/>',
		history:
			'<path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/><path d="M12 7v5l4 2"/>',
		inbox:
			'<polyline points="22 12 16 12 14 15 10 15 8 12 2 12"/><path d="M5.45 5.11 2 12v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-6l-3.45-6.89A2 2 0 0 0 16.76 4H7.24a2 2 0 0 0-1.79 1.11z"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'arrow-up-right': '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
		timer:
			'<line x1="10" x2="14" y1="2" y2="2"/><line x1="12" x2="15" y1="14" y2="11"/><circle cx="12" cy="14" r="8"/>'
	};

	type ActivityAction = 'approved' | 'rejected';

	type Activity = {
		id: string;
		action: ActivityAction;
		title: string;
		when: string;
	};

	type Stat = {
		label: string;
		value: string;
		icon: string;
		accent: 'amber' | 'green' | 'red' | 'ink';
	};

	// Realistic Mond data. Replace with load() data in production.
	const moderator = {
		name: 'Jonas Weber',
		email: 'jonas@mailbox.org',
		initials: 'JW'
	};

	const stats: Stat[] = [
		{ label: 'Pending reviews', value: '12', icon: 'hourglass', accent: 'amber' },
		{ label: 'Approved today', value: '7', icon: 'check', accent: 'green' },
		{ label: 'Rejected today', value: '2', icon: 'x', accent: 'red' },
		{ label: 'Avg. validation score', value: '0.86', icon: 'gauge', accent: 'ink' }
	];

	const recentActivity: Activity[] = [
		{ id: 'act_0841', action: 'approved', title: 'A Wizard of Earthsea', when: '2 minutes ago' },
		{ id: 'act_0840', action: 'rejected', title: 'Solaris', when: '18 minutes ago' },
		{ id: 'act_0839', action: 'approved', title: 'The Master and Margarita', when: '41 minutes ago' },
		{ id: 'act_0838', action: 'approved', title: 'Invisible Cities', when: '1 hour ago' },
		{ id: 'act_0837', action: 'rejected', title: 'Ficciones', when: '2 hours ago' }
	];

	const performance = {
		totalReviewed: 348,
		approvalRate: '91%',
		avgReviewTime: '4m 12s'
	};

	const accentStyles: Record<Stat['accent'], string> = {
		amber: 'border-[#F59E0B]/30 bg-[#F59E0B]/10 text-[#B45309]',
		green: 'border-[#22C55E]/30 bg-[#22C55E]/10 text-[#16A34A]',
		red: 'border-[#EF4444]/30 bg-[#EF4444]/10 text-[#DC2626]',
		ink: 'border-[#8B5CF6]/30 bg-[#8B5CF6]/10 text-[#6D28D9]'
	};

	const actionStyles: Record<ActivityAction, string> = {
		approved: 'border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]',
		rejected: 'border-[#EF4444]/40 bg-[#EF4444]/10 text-[#DC2626]'
	};

	const actionLabels: Record<ActivityAction, string> = {
		approved: 'Approved',
		rejected: 'Rejected'
	};

	const actionIcons: Record<ActivityAction, string> = {
		approved: 'check',
		rejected: 'x'
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

<svelte:head>
	<title>Moderator Dashboard — Mond</title>
	<meta
		name="description"
		content="The Mond moderator dashboard. Review pending contributor submissions before they become part of the public archive."
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
						href="/moderator"
						aria-current="page"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#18181B]"
					>
						{@render icon('shield-check', 15)}
						Moderation
					</a>
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
						href="/moderator/settings"
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
						href="/moderator/settings"
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
				href="/moderator"
				aria-current="page"
				class="flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#18181B]"
			>
				{@render icon('shield-check', 14)}
				Moderation
			</a>
			<a
				href="/dashboard"
				class="flex shrink-0 items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('layout-dashboard', 14)}
				Dashboard
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
			<!-- ============ WELCOME ============ -->
			<section aria-labelledby="welcome-heading">
				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Moderation
				</p>
				<h1
					id="welcome-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Moderator dashboard.
				</h1>
				<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
					Review pending contributor submissions before they become part of the
					public archive. Careful eyes are the archive&rsquo;s real infrastructure.
				</p>
			</section>

			<!-- ============ STATISTICS ============ -->
			<section aria-label="Moderation statistics" class="mt-12">
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

			<!-- ============ QUICK ACTIONS ============ -->
			<section aria-labelledby="actions-heading" class="mt-12">
				<div
					class="paper sealed rounded-lg p-8 text-center sm:flex sm:items-center sm:justify-between sm:p-10 sm:text-left"
				>
					<div>
						<p class="text-[11px] tracking-[0.25em] uppercase text-[#6D28D9]">
							Quick actions
						</p>
						<h2
							id="actions-heading"
							class="mt-3 text-2xl font-extralight tracking-tight text-[#18181B]"
						>
							The queue is waiting.
						</h2>
						<p class="mt-2 max-w-md text-sm font-light leading-relaxed text-[#52525B]">
							Twelve mappings await your judgement. Nothing enters the dataset
							without passing human review.
						</p>
					</div>
					<div class="mt-8 flex flex-col items-center gap-3 sm:mt-0 sm:ml-10 sm:shrink-0 sm:flex-row sm:gap-4">
						<a
							href="/moderator/queue"
							class="flex w-full items-center justify-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-7 py-3.5 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14] sm:w-auto"
						>
							{@render icon('inbox', 15)}
							Open review queue
						</a>
						<a
							href="/moderator/history"
							class="flex w-full items-center justify-center gap-2.5 rounded-md border border-[#E4E4E7] bg-white px-7 py-3.5 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05] sm:w-auto"
						>
							{@render icon('history', 15)}
							Review history
						</a>
					</div>
				</div>
			</section>

			<!-- ============ ACTIVITY + PERFORMANCE ============ -->
			<div class="mt-16 grid gap-8 lg:grid-cols-[1fr_320px]">
				<!-- ============ RECENT ACTIVITY ============ -->
				<section aria-labelledby="activity-heading">
					<div class="mb-6 flex items-end justify-between">
						<div>
							<p class="mb-2 text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]">
								— Your record —
							</p>
							<h2
								id="activity-heading"
								class="text-xl font-extralight tracking-tight text-[#18181B]"
							>
								Recent activity
							</h2>
						</div>
						<a
							href="/moderator/history"
							class="flex items-center gap-1.5 text-sm font-light text-[#71717A] transition-colors hover:text-[#18181B]"
						>
							View all
							{@render icon('arrow-up-right', 13)}
						</a>
					</div>

					<div class="paper rounded-lg p-6 sm:p-8">
						<ol class="relative">
							<!-- ink thread -->
							<div
								class="thread pointer-events-none absolute left-[13px] top-2 bottom-2 w-px"
								aria-hidden="true"
							></div>

							{#each recentActivity as activity, i (activity.id)}
								<li class="relative flex gap-5 {i < recentActivity.length - 1 ? 'pb-7' : ''}">
									<span
										class="relative z-10 flex h-7 w-7 shrink-0 items-center justify-center rounded-full border bg-white {actionStyles[activity.action]}"
									>
										{@render icon(actionIcons[activity.action], 11, 2.5)}
									</span>
									<div class="flex min-w-0 flex-1 items-baseline justify-between gap-4 pt-0.5">
										<div class="min-w-0">
											<p class="text-[11px] tracking-[0.2em] uppercase {activity.action === 'approved' ? 'text-[#16A34A]' : 'text-[#DC2626]'}">
												{actionLabels[activity.action]}
											</p>
											<p class="mt-1 truncate text-sm font-light text-[#18181B]">
												{activity.title}
											</p>
										</div>
										<span class="shrink-0 text-xs font-light text-[#A1A1AA]">
											{activity.when}
										</span>
									</div>
								</li>
							{/each}
						</ol>
					</div>
				</section>

				<!-- ============ PERFORMANCE SUMMARY ============ -->
				<section aria-labelledby="performance-heading">
					<div class="mb-6">
						<p class="mb-2 text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]">
							— All time —
						</p>
						<h2
							id="performance-heading"
							class="text-xl font-extralight tracking-tight text-[#18181B]"
						>
							Performance
						</h2>
					</div>

					<div class="paper rounded-lg p-6 sm:p-8">
						<dl class="space-y-6">
							<div class="flex items-center justify-between gap-4">
								<div class="flex items-center gap-3">
									<span
										class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/10 text-[#6D28D9]"
									>
										{@render icon('shield-check', 12, 2)}
									</span>
									<dt class="text-sm font-light text-[#52525B]">Total reviewed</dt>
								</div>
								<dd class="mono text-sm text-[#18181B]">{performance.totalReviewed}</dd>
							</div>

							<div class="border-t border-[#F4F4F5] pt-6">
								<div class="flex items-center justify-between gap-4">
									<div class="flex items-center gap-3">
										<span
											class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-[#22C55E]/30 bg-[#22C55E]/10 text-[#16A34A]"
										>
											{@render icon('check', 12, 2)}
										</span>
										<dt class="text-sm font-light text-[#52525B]">Approval rate</dt>
									</div>
									<dd class="mono text-sm text-[#18181B]">{performance.approvalRate}</dd>
								</div>
							</div>

							<div class="border-t border-[#F4F4F5] pt-6">
								<div class="flex items-center justify-between gap-4">
									<div class="flex items-center gap-3">
										<span
											class="flex h-7 w-7 shrink-0 items-center justify-center rounded-full border border-[#F59E0B]/30 bg-[#F59E0B]/10 text-[#B45309]"
										>
											{@render icon('timer', 12, 2)}
										</span>
										<dt class="text-sm font-light text-[#52525B]">Avg. review time</dt>
									</div>
									<dd class="mono text-sm text-[#18181B]">{performance.avgReviewTime}</dd>
								</div>
							</div>
						</dl>

						<blockquote class="quote mt-8 border-t border-[#F4F4F5] pt-6 text-[15px] leading-relaxed text-[#71717A]">
							&ldquo;Careful eyes are the archive&rsquo;s real infrastructure.&rdquo;
						</blockquote>
					</div>
				</section>
			</div>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light text-[#A1A1AA]">
				Every approved mapping strengthens the public archive.
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

	/* ---- Ink thread (activity timeline) ---- */
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
</style>