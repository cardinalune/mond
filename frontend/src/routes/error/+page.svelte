svelte
<!-- src/routes/+error.svelte -->
<script lang="ts">
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'layout-dashboard':
			'<rect width="7" height="9" x="3" y="3" rx="1"/><rect width="7" height="5" x="14" y="3" rx="1"/><rect width="7" height="9" x="14" y="12" rx="1"/><rect width="7" height="5" x="3" y="16" rx="1"/>',
		home: '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/>'
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
	<title>404 — Page not found — Mond</title>
	<meta name="description" content="The page you are looking for does not exist in the Mond archive." />
	<meta name="robots" content="noindex" />
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&family=Newsreader:ital,wght@1,300&family=JetBrains+Mono:wght@300;400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="page relative min-h-screen overflow-hidden bg-[#FAFAFA] text-[#18181B] antialiased">
	<!-- ============ DECORATIVE BACKGROUND ============ -->
	<!-- Soft radial wash behind the content -->
	<div class="glow pointer-events-none absolute inset-0" aria-hidden="true"></div>

	<!-- One large translucent crescent, upper-right, pure CSS -->
	<div class="crescent-lg pointer-events-none absolute" aria-hidden="true"></div>

	<!-- ============ NAV ============ -->
	<header class="absolute top-0 left-0 right-0 z-20">
		<nav class="mx-auto flex max-w-6xl items-center justify-between px-6 py-6">
			<a href="/" class="group flex items-center gap-3">
				<span class="crescent-sm" aria-hidden="true"></span>
				<span class="text-[15px] font-normal tracking-[0.22em] uppercase text-[#18181B]">
					Mond
				</span>
			</a>
		</nav>
	</header>

	<!-- ============ MAIN ============ -->
	<main class="relative z-10 flex min-h-screen items-center justify-center px-6 py-24">
		<section aria-labelledby="error-heading" class="fade-in mx-auto w-full max-w-lg text-center">
			<p class="fade-item text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]" style="--i: 0">
				Lost in the archive
			</p>

			<h1
				id="error-heading"
				class="fade-item mt-8 text-8xl font-extralight tracking-tight text-[#18181B] sm:text-9xl"
				style="--i: 1"
			>
				4<span class="text-[#6366F1]">0</span>4
			</h1>

			<p
				class="fade-item mx-auto mt-6 max-w-sm text-[15px] font-light leading-relaxed text-[#52525B]"
				style="--i: 2"
			>
				We couldn&rsquo;t find the page you&rsquo;re looking for.
			</p>

			<blockquote
				class="quote fade-item mx-auto mt-10 max-w-sm text-xl leading-snug text-[#71717A]"
				style="--i: 3"
			>
				&ldquo;Even the greatest libraries have missing shelves.&rdquo;
			</blockquote>

			<!-- Paper card with actions -->
			<div class="paper fade-item mx-auto mt-12 rounded-lg p-6 sm:p-8" style="--i: 4">
				<div class="flex flex-col items-center justify-center gap-3 sm:flex-row sm:gap-4">
					<a
						href="/"
						class="flex w-full items-center justify-center gap-2.5 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14] sm:w-auto"
					>
						{@render icon('home', 15)}
						Return home
					</a>
					<a
						href="/dashboard"
						class="flex w-full items-center justify-center gap-2.5 rounded-md border border-[#E4E4E7] bg-white px-6 py-3 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05] sm:w-auto"
					>
						{@render icon('layout-dashboard', 15)}
						Dashboard
					</a>
				</div>

				<p class="mono mt-6 border-t border-[#F4F4F5] pt-5 text-[11px] text-[#A1A1AA]">
					Error Code: 404_NOT_FOUND
				</p>
			</div>

			<p class="fade-item mt-14 text-xs font-light text-[#A1A1AA]" style="--i: 5">
				If you believe this record should exist, it may simply not have been catalogued yet.
			</p>
		</section>
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

	/* ---- Very soft radial wash behind the content ---- */
	.glow {
		background:
			radial-gradient(ellipse 60% 45% at 50% 42%, rgba(99, 102, 241, 0.055), transparent 65%),
			radial-gradient(ellipse 40% 30% at 50% 42%, rgba(139, 92, 246, 0.035), transparent 70%);
	}

	/* ---- Paper panel: light always falls from above ---- */
	.paper {
		background: #ffffff;
		border: 1px solid #e4e4e7;
		box-shadow:
			inset 0 1px 0 rgba(255, 255, 255, 0.9),
			0 1px 2px rgba(24, 24, 27, 0.04),
			0 16px 32px -20px rgba(24, 24, 27, 0.12);
	}

	/* ---- Lunar phase glyphs, drawn in ink (pure CSS) ---- */
	.crescent-sm {
		display: inline-block;
		height: 18px;
		width: 18px;
		border-radius: 9999px;
		box-shadow: inset -5px 3px 0 0 #6366f1;
	}

	/* Large translucent crescent, upper-right corner */
	.crescent-lg {
		top: -140px;
		right: -140px;
		height: 420px;
		width: 420px;
		border-radius: 9999px;
		box-shadow: inset -110px 70px 0 0 rgba(99, 102, 241, 0.06);
	}

	@media (min-width: 640px) {
		.crescent-lg {
			top: -160px;
			right: -100px;
			height: 560px;
			width: 560px;
			box-shadow: inset -150px 90px 0 0 rgba(99, 102, 241, 0.06);
		}
	}

	/* ---- Gentle staggered fade-in ---- */
	.fade-item {
		opacity: 0;
		animation: rise 0.9s cubic-bezier(0.22, 1, 0.36, 1) forwards;
		animation-delay: calc(var(--i, 0) * 120ms);
	}

	@keyframes rise {
		from {
			opacity: 0;
			transform: translateY(10px);
		}
		to {
			opacity: 1;
			transform: translateY(0);
		}
	}

	/* Respect users who prefer reduced motion */
	@media (prefers-reduced-motion: reduce) {
		.fade-item {
			animation: none;
			opacity: 1;
		}
	}
</style>