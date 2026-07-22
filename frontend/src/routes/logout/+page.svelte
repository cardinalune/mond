
<script lang="ts">
	import { goto } from "$app/navigation";
	import { user } from "$lib/stores/auth";

	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		'log-out':
			'<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/><polyline points="16 17 21 12 16 7"/><line x1="21" x2="9" y1="12" y2="12"/>',
		'arrow-right': '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
		check: '<path d="M20 6 9 17l-5-5"/>'
	};


	localStorage.removeItem("access_token");
	localStorage.removeItem("refresh_token");

	user.set(null);

	goto("/logout");
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
	<title>Signing out — Mond</title>
	<meta
		name="description"
		content="You have been signed out of Mond. Thank you for contributing to the preservation of public book metadata."
	/>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&family=Newsreader:ital,wght@1,300&family=JetBrains+Mono:wght@300;400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="page flex min-h-screen flex-col bg-[#FAFAFA] text-[#18181B] antialiased">
	<!-- ============ MINIMAL HEADER ============ -->
	<header class="absolute top-0 left-0 right-0 z-20">
		<div class="mx-auto flex max-w-6xl items-center justify-center px-6 py-8 sm:justify-start">
			<a href="/" class="group flex items-center gap-3">
				<span class="crescent-sm" aria-hidden="true"></span>
				<span class="text-[15px] font-normal tracking-[0.22em] uppercase text-[#18181B]">
					Mond
				</span>
			</a>
		</div>
	</header>

	<!-- ============ CENTERED CARD ============ -->
	<main class="morning flex flex-1 items-center justify-center px-6 py-32">
		<section aria-labelledby="logout-heading" class="w-full max-w-md">
			<div class="paper sealed rounded-lg p-8 text-center sm:p-12">
				<!-- Icon -->
				<div class="flex justify-center">
					<span
						class="flex h-14 w-14 items-center justify-center rounded-full border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] text-[#6D28D9]"
					>
						{@render icon('log-out', 20)}
					</span>
				</div>

				<!-- Heading -->
				<p class="mt-8 text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Session ended
				</p>
				<h1
					id="logout-heading"
					class="mt-3 text-3xl font-extralight tracking-tight text-[#18181B]"
				>
					Signing out
				</h1>

				<!-- Supporting text -->
				<p class="mx-auto mt-4 max-w-xs text-sm font-light leading-relaxed text-[#52525B]">
					Your Mond session has ended. Thank you for contributing to the
					preservation of public book metadata.
				</p>

				<!-- Quote -->
				<blockquote class="quote mx-auto mt-8 max-w-xs text-[17px] leading-relaxed text-[#3F3F46]">
					“Every contribution leaves the archive a little stronger.”
				</blockquote>

				<!-- Actions -->
				<div class="mt-10 flex flex-col items-center gap-3">
					<a
						href="/login"
						class="inline-flex w-full items-center justify-center gap-2 rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
					>
						Return to login
						{@render icon('arrow-right', 14)}
					</a>
					<a
						href="/"
						class="inline-flex w-full items-center justify-center rounded-md border border-[#E4E4E7] bg-white px-6 py-3 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
					>
						Back to home
					</a>
				</div>

				<!-- Session information -->
				<div class="mt-10 border-t border-[#F4F4F5] pt-6">
					<p
						class="flex items-center justify-center gap-2 text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
					>
						<span
							class="flex h-4 w-4 items-center justify-center rounded-full border border-[#22C55E]/40 bg-[#22C55E]/10 text-[#16A34A]"
						>
							{@render icon('check', 9, 2.5)}
						</span>
						Session terminated
					</p>
					<p class="mono mt-3 text-xs text-[#A1A1AA]">
						Authentication tokens have been cleared.
					</p>
					<p class="mt-1.5 text-xs font-light text-[#A1A1AA]">
						You may safely close this window.
					</p>
				</div>
			</div>
		</section>
	</main>

	<!-- ============ FOOTER ============ -->
	<footer class="border-t border-[#E4E4E7] bg-white px-6 py-10">
		<div class="mx-auto max-w-6xl text-center">
			<p class="text-xs font-light text-[#71717A]">Mond © 2026</p>
			<p class="mt-1.5 text-xs font-light text-[#A1A1AA]">
				Built quietly. Maintained openly.
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

	/* ---- Section washed with faint light from above ---- */
	.morning {
		background: radial-gradient(ellipse 70% 45% at 50% 0%, rgba(99, 102, 241, 0.045), transparent 65%);
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