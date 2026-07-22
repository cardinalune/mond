
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
		unlock:
			'<rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 9.9-1"/>',
		'git-branch':
			'<line x1="6" x2="6" y1="3" y2="15"/><circle cx="18" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M18 9a9 9 0 0 1-9 9"/>',
		'file-text':
			'<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M10 9H8"/><path d="M16 13H8"/><path d="M16 17H8"/>',
		'arrow-up-right': '<path d="M7 7h10v10"/><path d="M7 17 17 7"/>',
		'book-marked':
			'<path d="M10 2v8l3-3 3 3V2"/><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"/>'
	};

	type LicenseTerm = {
		label: string;
		value?: string;
	};

	const licenseTerms: LicenseTerm[] = [
		{ label: 'License', value: 'AGPL-3.0' },
		{ label: 'Source available' },
		{ label: 'Commercial use allowed' },
		{ label: 'Modification allowed' },
		{ label: 'Distribution allowed' },
		{ label: 'Patent grant included' },
		{ label: 'Network copyleft required' }
	];

	type Reason = {
		icon: string;
		title: string;
		desc: string;
	};

	const reasons: Reason[] = [
		{
			icon: 'unlock',
			title: 'Keeps improvements open',
			desc: 'Every change to Mond — bug fix, feature, or refinement — must remain available under the same license.'
		},
		{
			icon: 'shield-check',
			title: 'Prevents closed hosted forks',
			desc: 'Unlike permissive licenses, the AGPL applies even when the software is run as a network service. Hosted forks cannot go dark.'
		},
		{
			icon: 'users',
			title: 'Protects community contributions',
			desc: 'The work of contributors and moderators can never be enclosed inside a proprietary product.'
		},
		{
			icon: 'eye',
			title: 'Ensures transparency',
			desc: 'Anyone can read the exact code that validates, reviews, and publishes every mapping in the dataset.'
		},
		{
			icon: 'git-branch',
			title: 'Encourages collaboration',
			desc: 'Forks, experiments, and derivatives are welcome — as long as they give their improvements back.'
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
	<title>License — Mond</title>
	<meta
		name="description"
		content="Mond is free software released under the GNU Affero General Public License v3. The code, the dataset, and every improvement stay open — permanently."
	/>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&family=Newsreader:ital,wght@1,300&family=JetBrains+Mono:wght@300;400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="page min-h-screen bg-[#FAFAFA] text-[#18181B] antialiased">
	<!-- ============ WORDMARK ============ -->
	<div class="flex justify-center pt-12 sm:pt-16">
		<a href="/" class="flex items-center gap-3 text-[#18181B]">
			<span class="crescent-sm" aria-hidden="true"></span>
			<span class="text-sm tracking-[0.22em] uppercase">Mond</span>
		</a>
	</div>

	<main class="morning">
		<!-- ============ HERO ============ -->
		<section class="px-6 pt-20 sm:pt-24" aria-labelledby="license-heading">
			<div class="mx-auto max-w-3xl text-center">
				<p class="mb-6 text-[11px] font-normal tracking-[0.35em] uppercase text-[#71717A]">
					Open source
				</p>

				<h1
					id="license-heading"
					class="text-balance text-4xl font-extralight leading-[1.1] tracking-tight text-[#18181B] sm:text-5xl md:text-6xl"
				>
					Licensed for the
					<span class="text-[#6366F1]">public archive.</span>
				</h1>

				<p
					class="mx-auto mt-7 max-w-xl text-pretty text-[15px] font-light leading-relaxed text-[#52525B]"
				>
					Mond is an open-source project created to improve metadata quality for
					public book archives. Every approved contribution becomes part of a
					freely available dataset that anyone can inspect, improve, or build upon.
				</p>
			</div>
		</section>

		<!-- ============ LICENSE CARD ============ -->
		<section class="px-6 pt-16 sm:pt-20" aria-labelledby="agpl-heading">
			<div class="mx-auto max-w-2xl">
				<div class="paper sealed rounded-lg p-8 sm:p-12">
					<div class="flex items-center justify-between">
						<span
							class="flex items-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#6D28D9]"
						>
							{@render icon('scale', 13)}
							The license
						</span>
						<span class="mono text-[11px] text-[#A1A1AA]">SPDX: AGPL-3.0-only</span>
					</div>

					<h2
						id="agpl-heading"
						class="mt-8 text-2xl font-extralight tracking-tight text-[#18181B] sm:text-3xl"
					>
						GNU Affero General Public License v3
					</h2>

					<p class="mt-4 max-w-lg text-sm font-light leading-relaxed text-[#52525B]">
						Mond is released under the GNU AGPL v3. Any modifications deployed as
						a network service must also be made available under the same license.
					</p>

					<ul class="mt-10 divide-y divide-[#F4F4F5] border-t border-[#F4F4F5] pt-1">
						{#each licenseTerms as term}
							<li class="flex items-center justify-between gap-4 py-4">
								<span class="flex items-center gap-3.5 text-sm font-light text-[#3F3F46]">
									<span
										class="flex h-4 w-4 shrink-0 items-center justify-center rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]"
									>
										{@render icon('check', 9, 2.5)}
									</span>
									{term.label}
								</span>
								{#if term.value}
									<span class="mono text-xs text-[#6366F1]">{term.value}</span>
								{/if}
							</li>
						{/each}
					</ul>
				</div>
			</div>
		</section>

		<!-- ============ WHY AGPL ============ -->
		<section class="px-6 pt-28 sm:pt-36" aria-labelledby="why-heading">
			<div class="mx-auto max-w-2xl">
				<p class="mb-5 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					— Why AGPL —
				</p>
				<h2
					id="why-heading"
					class="text-balance text-center text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					A license chosen for durability.
				</h2>

				<div class="paper mt-14 overflow-hidden rounded-lg">
					<ul class="divide-y divide-[#F4F4F5]">
						{#each reasons as reason}
							<li class="flex gap-5 p-6 sm:gap-6 sm:p-8">
								<span
									class="mt-0.5 flex h-9 w-9 shrink-0 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] text-[#6D28D9]"
								>
									{@render icon(reason.icon, 15)}
								</span>
								<div>
									<h3 class="text-[15px] font-medium text-[#18181B]">{reason.title}</h3>
									<p class="mt-2 text-sm font-light leading-relaxed text-[#52525B]">
										{reason.desc}
									</p>
								</div>
							</li>
						{/each}
					</ul>
				</div>
			</div>
		</section>

		<!-- ============ PHILOSOPHY ============ -->
		<section class="px-6 pt-28 sm:pt-36" aria-labelledby="philosophy-heading">
			<div class="mx-auto max-w-3xl">
				<p class="mb-5 text-center text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					— Philosophy —
				</p>
				<h2
					id="philosophy-heading"
					class="text-balance text-center text-3xl font-extralight tracking-tight text-[#18181B] sm:text-4xl"
				>
					Built for preservation,<br class="hidden sm:block" /> not ownership.
				</h2>

				<div
					class="mx-auto mt-14 max-w-2xl space-y-7 text-[15px] font-light leading-[1.85] text-[#3F3F46]"
				>
					<p>
						Metadata is a common good. The record of which book is which — its
						editions, its identifiers, its provenance — should never belong to a
						single company or server. Mond publishes its entire dataset openly,
						so that the catalog can outlive any one host, and so that no one has
						to ask permission to know what a book is.
					</p>
					<p>
						The people who build this archive deserve to be seen. Every mapping
						carries its attribution, and every moderation decision is recorded in
						the open. Trust in an archive is not declared — it is earned through
						transparency, one reviewed record at a time.
					</p>
					<p>
						Anyone can read the source, audit the process, file an issue, or fork
						the project entirely. The AGPL guarantees that this remains true
						forever. Mond exists to preserve knowledge — not to become
						proprietary infrastructure around it.
					</p>
				</div>

				<blockquote
					class="quote mx-auto mt-20 max-w-xl text-center text-2xl leading-snug text-[#3F3F46] sm:mt-24 sm:text-3xl"
				>
					“What is freely given should stay freely given.”
				</blockquote>
			</div>
		</section>

		<!-- ============ REPOSITORY ============ -->
		<section class="px-6 pt-28 sm:pt-36" aria-labelledby="repo-heading">
			<div class="mx-auto max-w-2xl">
				<div
					class="paper sealed rounded-lg p-8 text-center sm:flex sm:items-center sm:justify-between sm:p-10 sm:text-left"
				>
					<div>
						<span
							class="flex items-center justify-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#6D28D9] sm:justify-start"
						>
							{@render icon('github', 13)}
							Repository
						</span>
						<h2 id="repo-heading" class="mono mt-5 text-lg font-light text-[#18181B] sm:text-xl">
							github.com/cardinalune/mond
						</h2>
						<p class="mt-3 max-w-md text-sm font-light leading-relaxed text-[#52525B]">
							Source code, issue tracker, documentation, roadmap, and
							contribution guidelines.
						</p>
					</div>
					<div class="mt-8 sm:mt-0 sm:ml-12 sm:shrink-0">
						<a
							href="https://github.com/cardinalune/mond?"
							class="inline-flex items-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
						>
							View repository
							{@render icon('arrow-up-right', 14)}
						</a>
					</div>
				</div>
			</div>
		</section>

		<!-- ============ OFFICIAL LICENSE TEXT ============ -->
		<section class="px-6 pt-6 pb-28 sm:pb-36" aria-labelledby="full-license-heading">
			<div class="mx-auto max-w-2xl">
				<div class="paper rounded-lg p-8 text-center sm:p-12">
					<div class="mb-6 flex justify-center text-[#6366F1]">
						{@render icon('file-text', 20)}
					</div>
					<h2
						id="full-license-heading"
						class="text-xl font-extralight tracking-tight text-[#18181B] sm:text-2xl"
					>
						Official License Text
					</h2>
					<p class="mx-auto mt-4 max-w-md text-sm font-light leading-relaxed text-[#52525B]">
						The complete GNU Affero General Public License v3 is included with
						every copy of Mond. This page provides a summary only. For the
						legally binding license text, read the official
						<span class="mono text-xs text-[#3F3F46]">LICENSE</span>
						file included in the repository.
					</p>

					<div
						class="mt-10 flex flex-col items-center justify-center gap-3 sm:flex-row sm:gap-4"
					>
						<a
							href="https://www.gnu.org/licenses/agpl-3.0.html"
							class="inline-flex w-full items-center justify-center gap-2 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14] sm:w-auto"
						>
							{@render icon('scale', 15)}
							Read full license
						</a>
						<a
							href="https://github.com/cardinalune/mond/blob/main/LICENSE"
							class="inline-flex w-full items-center justify-center gap-2 rounded-md border border-[#E4E4E7] bg-white px-6 py-3 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05] sm:w-auto"
						>
							{@render icon('github', 15)}
							View LICENSE on GitHub
						</a>
					</div>
				</div>

				<p class="mt-8 text-center text-xs font-light text-[#A1A1AA]">
					This summary is provided for convenience and is not legal advice.
				</p>
			</div>
		</section>
	</main>

	<!-- ============ FOOTER ============ -->
	<footer class="border-t border-[#E4E4E7] bg-white px-6 py-16">
		<div class="mx-auto max-w-6xl text-center">
			<div class="flex items-center justify-center gap-3">
				<span class="crescent-sm" aria-hidden="true"></span>
				<span class="text-sm font-normal tracking-[0.22em] uppercase text-[#18181B]">Mond</span>
			</div>
			<p class="mt-6 text-xs font-light leading-relaxed text-[#71717A]">
				Mond © 2026 · Released under GNU AGPL v3.
			</p>
			<p class="mt-2 text-xs font-light text-[#A1A1AA]">
				Built for the public archive.
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

	/* ---- Lunar crescent glyph, drawn in ink (pure CSS) ---- */
	.crescent-sm {
		display: inline-block;
		height: 18px;
		width: 18px;
		border-radius: 9999px;
		box-shadow: inset -5px 3px 0 0 #6366f1;
	}
</style>