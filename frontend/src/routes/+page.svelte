<script lang="ts">
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		github:
			'<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/>',
		check: '<path d="M20 6 9 17l-5-5"/>',
		'shield-check':
			'<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
		scale:
			'<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
		users:
			'<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
		eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
		upload:
			'<path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="17 8 12 3 7 8"/><line x1="12" x2="12" y1="3" y2="15"/>',
		'search-check':
			'<path d="m8 11 2 2 4-4"/><circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
		'file-down':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
		'arrow-down': '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>',
		library: '<path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/>'
	};

	type Station = {
		icon: string;
		title: string;
		desc: string;
	};

	const stations: Station[] = [
		{
			icon: 'upload',
			title: 'Submit',
			desc: 'Propose a mapping between an MD5 record and an Open Library edition.'
		},
		{
			icon: 'search-check',
			title: 'Validate',
			desc: 'Automated checks normalize titles, verify ISBN checksums, and compare fields.'
		},
		{
			icon: 'shield-check',
			title: 'Review',
			desc: 'A human moderator reads every submission before it is accepted. No exceptions.'
		},
		{
			icon: 'file-down',
			title: 'Export',
			desc: 'Verified Mappings join the public dataset — free to download, forever.'
		}
	];

	const validationChecks: string[] = [
		'Title normalized and matched',
		'Author name matched',
		'ISBN-13 checksum valid',
		'Publication year consistent'
	];

	const openItems: { icon: string; title: string; desc: string }[] = [
		{
			icon: 'scale',
			title: 'AGPL-3.0 licensed',
			desc: 'The code, and every improvement to it, stays free — even when run as a service.'
		},
		{
			icon: 'github',
			title: 'Source in the open',
			desc: 'Development happens in public. Issues, decisions, and history are visible to all.'
		},
		{
			icon: 'users',
			title: 'Community maintained',
			desc: 'No company behind it. Contributors and moderators keep the archive alive.'
		},
		{
			icon: 'eye',
			title: 'Transparent review',
			desc: 'Every moderation decision is recorded.'
		}
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

<svelte:head>
	<title>Mond — Preserving book metadata through community verification</title>
	<meta
		name="description"
		content="Mond is an open-source archive that maps MD5 records to Open Library editions. Every mapping is verified by human moderators."
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
	<header class="absolute top-0 left-0 right-0 z-20">
		<nav class="mx-auto flex max-w-6xl items-center justify-between px-6 py-6">
			<a href="/" class="group flex items-center gap-3">
				<span class="crescent-sm" aria-hidden="true"></span>
				<span class="text-[15px] font-normal tracking-[0.22em] uppercase text-[#18181B]">
					Mond
				</span>
			</a>

			<div class="flex items-center gap-1 sm:gap-2">
				<a
					href="https://github.com/cardinalune/mond?"
					class="flex items-center gap-2 rounded-md px-3 py-2 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
					aria-label="GitHub repository"
				>
					{@render icon('github', 16)}
					<span class="hidden sm:inline">GitHub</span>
				</a>
				<a
					href="/login"
					class="rounded-md px-3 py-2 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
				>
					Login
				</a>
				<a
					href="/register"
					class="rounded-md border border-[#E4E4E7] bg-white px-4 py-2 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
				>
					Create account
				</a>
			</div>
		</nav>
	</header>

	<!-- ============ HERO ============ -->
	<section class="daylight relative flex min-h-screen flex-col items-center justify-end overflow-hidden px-6 pb-28">
		<div class="relative z-10 mx-auto max-w-3xl text-center">
			<p class="mb-8 text-[11px] font-normal tracking-[0.35em] uppercase text-[#71717A]">
				Open metadata infrastructure
			</p>

			<h1 class="text-balance text-5xl font-extralight leading-[1.08] tracking-tight text-[#18181B] sm:text-6xl md:text-7xl">
				Knowledge deserves
				<br />
				<span class="text-[#6366F1]">careful verification.</span>
			</h1>

			<p class="mx-auto mt-8 max-w-xl text-pretty text-[15px] font-light leading-relaxed text-[#52525B]">
				Mond preserves verified mappings between MD5 fingerprints and Open Library editions.
				Every mapping is reviewed by a human moderator before it enters
				the public dataset.
			</p>

			<div class="mt-12 flex items-center justify-center gap-6">
				<a
					href="/register"
					class="rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
				>
					Start contributing
				</a>
				<a
					href="https://github.com/cardinalune/mond?"
					class="flex items-center gap-2 text-sm text-[#71717A] transition-colors hover:text-[#18181B]"
				>
					{@render icon('github', 15)}
					Read the source
				</a>
			</div>
		</div>

		<div class="pointer-events-none absolute bottom-8 left-1/2 -translate-x-1/2 text-[#A1A1AA]">
			{@render icon('arrow-down', 16, 1)}
		</div>
	</section>

	<!-- ============ CENTERPIECE: THE RECORD ============ -->
	<section class="relative px-6 py-36">
		<div class="mx-auto max-w-2xl">
			<p class="mb-4 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
				— The record —
			</p>
			<h2 class="text-balance text-center text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl">
				One mapping, from submission to seal.
			</h2>
			<p class="mx-auto mt-5 max-w-md text-center text-sm font-light leading-relaxed text-[#52525B]">
				This is the entire journey of a single record through Mond.
				Nothing enters the dataset without passing every stage.
			</p>

			<!-- The descending chain -->
			<div class="relative mt-20">
				<!-- ink thread -->
				<div class="thread pointer-events-none absolute left-1/2 top-0 h-full w-px -translate-x-1/2" aria-hidden="true"></div>

				<!-- Panel 1: MD5 Record -->
				<div class="paper relative rounded-lg p-6 sm:p-8">
					<div class="mb-5 flex items-center justify-between">
						<span class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
							{@render icon('book-marked', 13)}
							MD5 record
						</span>
						<span class="mono text-[11px] text-[#A1A1AA]">source</span>
					</div>
					<p class="text-xl font-light text-[#18181B]">The Left Hand of Darkness</p>
					<p class="mt-1 text-sm font-light text-[#52525B]">Ursula K. Le Guin · epub · 1969</p>
					<p class="mono mt-4 text-xs text-[#A1A1AA]">
						md5&nbsp;&nbsp;f2b4d1a9c07e83aa41c6…9e12
					</p>
				</div>

				<div class="connector" aria-hidden="true">
					<span class="connector-node">{@render icon('arrow-down', 11)}</span>
				</div>

				<!-- Panel 2: Metadata Validation -->
				<div class="paper relative rounded-lg p-6 sm:p-8">
					<div class="mb-5">
						<span class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
							{@render icon('search-check', 13)}
							Metadata validation
						</span>
					</div>
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

				<div class="connector" aria-hidden="true">
					<span class="connector-node">{@render icon('arrow-down', 11)}</span>
				</div>

				<!-- Panel 3: Open Library Edition -->
				<div class="paper relative rounded-lg p-6 sm:p-8">
					<div class="mb-5 flex items-center justify-between">
						<span class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
							{@render icon('library', 13)}
							Open Library edition
						</span>
						<span class="mono text-[11px] text-[#A1A1AA]">target</span>
					</div>
					<p class="mono text-lg font-light text-[#6366F1]">OL7602281M</p>
					<p class="mt-2 text-sm font-light text-[#52525B]">
						Ace Books · 1969 · ISBN 978-0-441-47812-5
					</p>
				</div>

				<div class="connector" aria-hidden="true">
					<span class="connector-node">{@render icon('arrow-down', 11)}</span>
				</div>

				<!-- Panel 4: Moderator Review -->
				<div class="paper relative rounded-lg p-6 sm:p-8">
					<div class="mb-5 flex items-center justify-between">
						<span class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]">
							{@render icon('shield-check', 13)}
							Moderator review
						</span>
						<span class="rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 px-2.5 py-0.5 text-[11px] text-[#16A34A]">
							Verified
						</span>
					</div>
					<blockquote class="quote text-[15px] leading-relaxed text-[#3F3F46]">
						“Edition matches the first Ace paperback printing. ISBN confirmed
						against the Open Library record. Approving.”
					</blockquote>
					<p class="mono mt-4 text-xs text-[#A1A1AA]">reviewed by a community moderator</p>
				</div>

				<div class="connector" aria-hidden="true">
					<span class="connector-node">{@render icon('arrow-down', 11)}</span>
				</div>

				<!-- Panel 5: Verified Mapping (sealed) -->
				<div class="paper sealed relative rounded-lg p-6 text-center sm:p-10">
					<span class="text-[11px] tracking-[0.25em] uppercase text-[#6D28D9]">
						Verified Mapping
					</span>
					<p class="mono mt-5 text-sm text-[#18181B] sm:text-base">
						f2b4d1a9…9e12
						<span class="mx-3 text-[#8B5CF6]">↔</span>
						OL7602281M
					</p>
					<p class="mt-4 text-xs font-light text-[#71717A]">
						Entered into the public dataset. Permanent, attributed, and free.
					</p>
				</div>
			</div>
		</div>
	</section>

	<!-- ============ PHILOSOPHY ============ -->
	<section class="morning relative px-6 py-36">
		<div class="mx-auto max-w-5xl">
			<p class="mb-4 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
				— Why we work this way —
			</p>
			<h2 class="text-balance text-center text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl">
				Slow, deliberate, and human.
			</h2>

			<div class="mt-20 grid gap-14 sm:grid-cols-3 sm:gap-10">
				<div class="text-center sm:text-left">
					<div class="mb-6 flex justify-center sm:justify-start">
						<span class="phase-crescent" aria-hidden="true"></span>
					</div>
					<h3 class="text-lg font-normal text-[#18181B]">Preserve</h3>
					<p class="mt-3 text-sm font-light leading-relaxed text-[#52525B]">
						Metadata decays quietly. Titles drift, editions blur, links rot.
						A book that cannot be found is a book that is lost — no matter how
						many copies survive.
					</p>
				</div>

				<div class="text-center sm:text-left">
					<div class="mb-6 flex justify-center sm:justify-start">
						<span class="phase-half" aria-hidden="true"></span>
					</div>
					<h3 class="text-lg font-normal text-[#18181B]">Verify</h3>
					<p class="mt-3 text-sm font-light leading-relaxed text-[#52525B]">
						Automation catches errors; it does not create trust. Every mapping
						in Mond is read by a person before it is accepted. Careful eyes are
						the archive’s real infrastructure.
					</p>
				</div>

				<div class="text-center sm:text-left">
					<div class="mb-6 flex justify-center sm:justify-start">
						<span class="phase-full" aria-hidden="true"></span>
					</div>
					<h3 class="text-lg font-normal text-[#18181B]">Publish</h3>
					<p class="mt-3 text-sm font-light leading-relaxed text-[#52525B]">
						The dataset belongs to everyone. It is exportable in full, versioned
						in the open, and carries its provenance with it — so it can outlive
						any single server, or any of us.
					</p>
				</div>
			</div>

			<blockquote class="quote mx-auto mt-28 max-w-xl text-center text-2xl leading-snug text-[#3F3F46] sm:text-3xl">
				“A library is only as durable as its catalog.”
			</blockquote>
		</div>
	</section>

	<!-- ============ WORKFLOW ============ -->
	<section class="relative px-6 py-36">
		<div class="mx-auto max-w-5xl">
			<p class="mb-4 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
				— The workflow —
			</p>
			<h2 class="text-balance text-center text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl">
				Four stages. No shortcuts.
			</h2>

			<div class="relative mt-24">
				<!-- meridian line -->
				<div class="meridian pointer-events-none absolute left-8 top-0 h-full w-px sm:left-0 sm:top-[22px] sm:h-px sm:w-full" aria-hidden="true"></div>

				<ol class="grid gap-14 sm:grid-cols-4 sm:gap-8">
					{#each stations as station, i}
						<li class="relative flex gap-6 pl-0 sm:block">
							<div class="relative z-10 flex h-11 w-11 shrink-0 items-center justify-center rounded-full border border-[#E4E4E7] bg-white text-[#6366F1] shadow-sm sm:mb-6">
								{@render icon(station.icon, 16)}
							</div>
							<div>
								<p class="mono mb-1 text-[11px] text-[#A1A1AA]">
									0{i + 1}
								</p>
								<h3 class="text-base font-medium text-[#18181B]">{station.title}</h3>
								<p class="mt-2 text-sm font-light leading-relaxed text-[#52525B]">
									{station.desc}
								</p>
							</div>
						</li>
					{/each}
				</ol>
			</div>
		</div>
	</section>

	<!-- ============ OPEN SOURCE ============ -->
	<section class="morning relative px-6 py-36">
		<div class="mx-auto max-w-4xl">
			<p class="mb-4 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
				— Open source —
			</p>
			<h2 class="text-balance text-center text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl">
				Open by principle,<br class="hidden sm:block" /> not by fashion.
			</h2>
			<p class="mx-auto mt-6 max-w-lg text-center text-sm font-light leading-relaxed text-[#52525B]">
				An archive you cannot inspect is an archive you cannot trust.
				Mond’s code, data, and moderation history are open — permanently.
			</p>

			<div class="mt-16 grid gap-px overflow-hidden rounded-lg border border-[#E4E4E7] bg-[#E4E4E7] shadow-sm sm:grid-cols-2">
				{#each openItems as item}
					<div class="bg-white p-8">
						<div class="mb-4 text-[#6366F1]">
							{@render icon(item.icon, 18)}
						</div>
						<h3 class="text-[15px] font-medium text-[#18181B]">{item.title}</h3>
						<p class="mt-2 text-sm font-light leading-relaxed text-[#52525B]">
							{item.desc}
						</p>
					</div>
				{/each}
			</div>

			<div class="mt-14 flex justify-center">
				<a
					href="https://github.com/cardinalune/mond?"
					class="flex items-center gap-2.5 rounded-md border border-[#E4E4E7] bg-white px-6 py-3 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
				>
					{@render icon('github', 16)}
					View the repository
				</a>
			</div>
		</div>
	</section>

	<!-- ============ FOOTER ============ -->
	<footer class="border-t border-[#E4E4E7] bg-white px-6 py-16">
		<div class="mx-auto flex max-w-6xl flex-col items-center gap-10 sm:flex-row sm:items-start sm:justify-between">
			<div>
				<div class="flex items-center gap-3">
					<span class="crescent-sm" aria-hidden="true"></span>
					<span class="text-sm font-normal tracking-[0.22em] uppercase text-[#18181B]">Mond</span>
				</div>
				<p class="mt-4 max-w-xs text-xs font-light leading-relaxed text-[#71717A]">
					<span class="italic">Mond</span> — German for “Moon.”
					A quiet archive of verified book metadata.
				</p>
			</div>

			<div class="flex gap-16 text-sm">
				<div class="flex flex-col gap-3">
					<span class="text-[11px] tracking-[0.25em] uppercase text-[#A1A1AA]">Project</span>
					<a href="https://github.com" class="font-light text-[#71717A] transition-colors hover:text-[#18181B]">GitHub</a>
					<a href="/license" class="font-light text-[#71717A] transition-colors hover:text-[#18181B]">License (AGPL-3.0)</a>
				</div>
				
			</div>
		</div>

		<div class="mx-auto mt-16 max-w-6xl border-t border-[#F4F4F5] pt-8">
			<p class="text-center text-xs font-light text-[#A1A1AA]">
				Built quietly. Maintained openly. Mond is free software under the AGPL-3.0 license.
			</p>
		</div>
	</footer>
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

	/* ---- Daylight: morning sun through a tall window, above ---- */
	.daylight {
		background:
			radial-gradient(ellipse 90% 55% at 50% -18%, rgba(99, 102, 241, 0.1), transparent 62%),
			radial-gradient(ellipse 45% 30% at 50% -10%, rgba(139, 92, 246, 0.07), transparent 70%),
			linear-gradient(to bottom, #f6f6fa, #fafafa);
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

	/* ---- Ink thread & connectors ---- */
	.thread {
		background: linear-gradient(
			to bottom,
			transparent,
			rgba(99, 102, 241, 0.3) 12%,
			rgba(99, 102, 241, 0.3) 88%,
			transparent
		);
	}

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

	/* ---- Meridian line (workflow) ---- */
	.meridian {
		background: linear-gradient(
			to right,
			transparent,
			rgba(99, 102, 241, 0.25) 15%,
			rgba(99, 102, 241, 0.25) 85%,
			transparent
		);
	}

	@media (max-width: 639px) {
		.meridian {
			background: linear-gradient(
				to bottom,
				transparent,
				rgba(99, 102, 241, 0.25) 10%,
				rgba(99, 102, 241, 0.25) 90%,
				transparent
			);
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

	.phase-half {
		display: inline-block;
		height: 32px;
		width: 32px;
		border-radius: 9999px;
		border: 1px solid rgba(99, 102, 241, 0.4);
		background: linear-gradient(90deg, transparent 50%, #6366f1 50%);
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