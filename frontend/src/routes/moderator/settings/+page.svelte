
<script lang="ts">
	import { user, authLoading } from "$lib/stores/auth";
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'layout-dashboard':
			'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
		'file-down':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
		settings:
			'<path d="M12.22 2h-.44a2 2 0 0 0-2 2v.18a2 2 0 0 1-1 1.73l-.43.25a2 2 0 0 1-2 0l-.15-.08a2 2 0 0 0-2.73.73l-.22.38a2 2 0 0 0 .73 2.73l.15.1a2 2 0 0 1 1 1.72v.51a2 2 0 0 1-1 1.74l-.15.09a2 2 0 0 0-.73 2.73l.22.38a2 2 0 0 0 2.73.73l.15-.08a2 2 0 0 1 2 0l.43.25a2 2 0 0 1 1 1.73V20a2 2 0 0 0 2 2h.44a2 2 0 0 0 2-2v-.18a2 2 0 0 1 1-1.73l.43-.25a2 2 0 0 1 2 0l.15.08a2 2 0 0 0 2.73-.73l.22-.39a2 2 0 0 0-.73-2.73l-.15-.08a2 2 0 0 1-1-1.74v-.5a2 2 0 0 1 1-1.74l.15-.09a2 2 0 0 0 .73-2.73l-.22-.38a2 2 0 0 0-2.73-.73l-.15.08a2 2 0 0 1-2 0l-.43-.25a2 2 0 0 1-1-1.73V4a2 2 0 0 0-2-2z"/><circle cx="12" cy="12" r="3"/>',
		user: '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		'chevron-down': '<path d="m6 9 6 6 6-6"/>',
		lock: '<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
		'shield-check':
			'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
		scale:
			'<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>'
	};

	// Realistic Mond data.

	function getInitials(name: string) {
    return name
        .split(" ")
        .map((part) => part[0])
        .join("")
        .slice(0, 2)
        .toUpperCase();
	}

	const about = {
		version: 'MVP',
		license: 'AGPL-3.0'
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

{#snippet sectionLabel(text: string, iconName: string)}
	<span class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
		{@render icon(iconName, 13)}
		{text}
	</span>
{/snippet}

<svelte:head>
	<title>Settings — Mond</title>
	<meta name="description" content="Manage your Mond account and session." />
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
						href="/dashboard/settings"
						aria-current="page"
						class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#18181B]"
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
						href="/dashboard/settings"
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
				href="/dashboard/settings"
				aria-current="page"
				class="flex items-center gap-2 rounded-md px-3 py-1.5 text-sm text-[#18181B]"
			>
				{@render icon('settings', 14)}
				Settings
			</a>
		</div>
	</header>

	<main class="morning">
		<div class="mx-auto max-w-2xl px-6 pb-28 pt-14 sm:pt-20">
			<!-- ============ HEADER ============ -->
			<section aria-labelledby="settings-heading">
				<p class="mb-3 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Account
				</p>
				<h1
					id="settings-heading"
					class="text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Settings
				</h1>
				<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
					Manage your Mond account and session.
				</p>
			</section>

			<!-- ============ PROFILE ============ -->
			<section aria-labelledby="profile-heading" class="mt-12">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6 flex items-center justify-between">
						<h2 id="profile-heading" class="sr-only">Profile</h2>
						{@render sectionLabel('Profile', 'user')}
					</div>

					<dl class="divide-y divide-[#F4F4F5]">
						<div class="flex items-baseline justify-between gap-6 py-3.5 first:pt-0">
							<dt class="text-sm font-light text-[#71717A]">Username</dt>
							<dd class="mono text-sm text-[#3F3F46]">{$user?.username}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-6 py-3.5">
							<dt class="text-sm font-light text-[#71717A]">Email</dt>
							<dd class="mono text-sm text-[#3F3F46]">{$user?.email}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-6 py-3.5">
							<dt class="text-sm font-light text-[#71717A]">Role</dt>
							<dd>
								<span
									class="inline-flex items-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/10 px-2.5 py-0.5 text-[11px] text-[#6D28D9]"
								>
									{#if $user?.role === "user"}
										Contributor
									{:else if $user?.role === "moderator"}
										Moderator
									{:else if $user?.role === "admin"}
										Administrator
									{/if}
								</span>
							</dd>
						</div>
						<div class="flex items-baseline justify-between gap-6 py-3.5 last:pb-0">
							<dt class="text-sm font-light text-[#71717A]">Member since</dt>
							<dd class="text-sm font-light text-[#3F3F46]">----</dd>
						</div>
					</dl>
				</div>
			</section>

			<!-- ============ SECURITY ============ -->
			<section aria-labelledby="security-heading" class="mt-8">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6">
						<h2 id="security-heading" class="sr-only">Security</h2>
						{@render sectionLabel('Security', 'lock')}
					</div>

					<div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
						<div>
							<p class="text-sm text-[#18181B]">Password</p>
							<p class="mt-1 text-sm font-light leading-relaxed text-[#52525B]">
								Update the password you use to sign in.
							</p>
						</div>
						<div class="sm:shrink-0 sm:text-right">
							<button
								type="button"
								disabled
								class="inline-flex cursor-not-allowed items-center gap-2 rounded-md border border-[#E4E4E7] bg-[#F4F4F5] px-5 py-2.5 text-sm text-[#A1A1AA]"
							>
								{@render icon('lock', 14)}
								Change password
							</button>
							<p class="mt-2 text-xs font-light text-[#A1A1AA]">Coming soon.</p>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ SESSION ============ -->
			<section aria-labelledby="session-heading" class="mt-8">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6">
						<h2 id="session-heading" class="sr-only">Session</h2>
						{@render sectionLabel('Session', 'shield-check')}
					</div>

					<div class="flex flex-col gap-4 sm:flex-row sm:items-center sm:justify-between">
						<div>
							<p class="text-sm text-[#18181B]">Current session</p>
							<p class="mt-1.5 flex items-center gap-2 text-sm font-light text-[#52525B]">
								<span
									class="inline-flex items-center gap-1.5 rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 px-2.5 py-0.5 text-[11px] text-[#16A34A]"
								>
									Signed in
								</span>
							</p>
						</div>
						<div class="sm:shrink-0">
							<a
								href="/logout"
								class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-5 py-2.5 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
							>
								{@render icon('log-out', 14)}
								Sign out
							</a>
						</div>
					</div>
				</div>
			</section>

			<!-- ============ ABOUT MOND ============ -->
			<section aria-labelledby="about-heading" class="mt-8">
				<div class="paper rounded-lg p-6 sm:p-8">
					<div class="mb-6">
						<h2 id="about-heading" class="sr-only">About Mond</h2>
						{@render sectionLabel('About Mond', 'book-marked')}
					</div>

					<dl class="divide-y divide-[#F4F4F5]">
						<div class="flex items-baseline justify-between gap-6 py-3.5 first:pt-0">
							<dt class="text-sm font-light text-[#71717A]">Version</dt>
							<dd class="mono text-sm text-[#3F3F46]">{about.version}</dd>
						</div>
						<div class="flex items-baseline justify-between gap-6 py-3.5">
							<dt class="flex items-center gap-2 text-sm font-light text-[#71717A]">
								{@render icon('scale', 13)}
								License
							</dt>
							<dd class="mono text-sm text-[#6366F1]">{about.license}</dd>
						</div>
					</dl>

					<p class="mt-6 border-t border-[#F4F4F5] pt-6 text-sm font-light leading-relaxed text-[#52525B]">
						<span class="italic">Mond</span> — German for “Moon” — is a quiet, open archive
						that preserves verified links between Anna’s Archive books and Open Library
						editions. Every mapping is reviewed by a human moderator before it enters
						the public record.
					</p>
				</div>
			</section>

			<!-- ============ QUIET FOOTNOTE ============ -->
			<p class="mt-20 text-center text-xs font-light text-[#A1A1AA]">
				Built quietly. Maintained openly. Mond is free software under the AGPL-3.0 license.
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