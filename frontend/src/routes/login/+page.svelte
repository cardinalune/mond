<script lang="ts">
import { login } from "$lib/api/auth";
import type { LoginRequest } from "$lib/types/auth";
import { goto } from "$app/navigation";
import {
	loadCurrentUser,
	user,
} from "$lib/stores/auth";

import { get } from "svelte/store";
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		github:
			'<path d="M15 22v-4a4.8 4.8 0 0 0-1-3.5c3 0 6-2 6-5.5.08-1.25-.27-2.48-1-3.5.28-1.15.28-2.35 0-3.5 0 0-1 0-3 1.5-2.64-.5-5.36-.5-8 0C6 2 5 2 5 2c-.3 1.15-.3 2.35 0 3.5A5.403 5.403 0 0 0 4 9c0 3.5 3 5.5 6 5.5-.39.49-.68 1.05-.85 1.65-.17.6-.22 1.23-.15 1.85v4"/><path d="M9 18c-4.51 2-5-2-7-2"/>',
		eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
		'eye-off':
			'<path d="M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49"/><path d="M14.084 14.158a3 3 0 0 1-4.242-4.242"/><path d="M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143"/><path d="m2 2 20 20"/>',
		'arrow-left': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>'
	};

	let email = $state('');
	let password = $state('');

	let showPassword = $state(false);

	let loading = $state(false);
	let error = $state("");

	async function handleSubmit(event: SubmitEvent) {
	event.preventDefault();

	error = "";
	loading = true;

	try {
		const payload: LoginRequest = {
			email,
			password,
		};

		const response = await login(payload);

		localStorage.setItem(
			"access_token",
			response.access_token
		);

		localStorage.setItem(
			"refresh_token",
			response.refresh_token
		);

		await loadCurrentUser();

		const currentUser = get(user);

		if (currentUser?.role === "admin" ||
			currentUser?.role === "moderator") {

			await goto("/moderator");

		} else {

			await goto("/dashboard");

		}


	} catch (err) {
		error = err instanceof Error
			? err.message
			: "Something went wrong.";
	} finally {
		loading = false;
	}
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

<svelte:head>
	<title>Sign in — Mond</title>
	<meta
		name="description"
		content="Sign in to your Mond account to contribute verified book metadata mappings."
	/>
	<link rel="preconnect" href="https://fonts.googleapis.com" />
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="anonymous" />
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500&family=Newsreader:ital,wght@1,300&family=JetBrains+Mono:wght@300;400&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<div class="page flex min-h-screen flex-col bg-[#FAFAFA] text-[#18181B] antialiased">
	<!-- ============ QUIET RETURN LINK ============ -->
	<header class="absolute top-0 left-0 right-0 z-20">
		<nav class="mx-auto flex max-w-6xl items-center justify-between px-6 py-6">
			<a
				href="/"
				class="flex items-center gap-2 text-sm font-light text-[#71717A] transition-colors hover:text-[#18181B]"
			>
				{@render icon('arrow-left', 14)}
				Back to Mond
			</a>
			<a
				href="/register"
				class="rounded-md border border-[#E4E4E7] bg-white px-4 py-2 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
			>
				Create account
			</a>
		</nav>
	</header>

	<!-- ============ CENTERED CARD ============ -->
	<main class="daylight flex flex-1 items-center justify-center px-6 py-28">
		<div class="w-full max-w-sm">
			<!-- Moon branding above the card -->
			<div class="mb-10 flex flex-col items-center">
				<a href="/" class="flex flex-col items-center gap-4" aria-label="Mond home">
					<span class="crescent-lg" aria-hidden="true"></span>
					<span class="text-[13px] font-normal tracking-[0.28em] uppercase text-[#18181B]">
						Mond
					</span>
				</a>
			</div>

			<div class="paper rounded-lg p-8  sm:p-10">
				<p class="text-[11px] tracking-[0.35em] uppercase text-center text-[#A1A1AA]">
					Open metadata begins with trust
				</p>
				<h1 class="mt-5 text-3xl font-extralight tracking-tight text-center text-[#18181B]">
					Sign in
				</h1>
				<p class="mt-4 text-sm font-light leading-relaxed text-center text-[#52525B]">
					Sign in using your Mond account.
				</p>

				<form class="mt-10 space-y-6" onsubmit={handleSubmit}>


					<!-- Error Box -->
					{#if error}
						<div
							class="rounded-md border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700"
						>
							{error}
						</div>
					{/if}



					<!-- Email -->
					<div>
						<label
							for="email"
							class="mb-2.5 block text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							Email
						</label>
						<input
							id="email"
							name="email"
							type="email"
							bind:value={email}
							required
							autocomplete="email"
							placeholder="you@example.org"
							class="field w-full rounded-md px-4 py-3 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA]"
						/>
					</div>

					<!-- Password -->
					<div>
						<div class="mb-2.5 flex items-baseline justify-between">
							<label
								for="password"
								class="block text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
							>
								Password
							</label>
							<!--
							<a
								href="/forgot-password"
								class="text-xs font-light text-[#71717A] transition-colors hover:text-[#6D28D9]"
							>
								Forgot password?
							</a>
							-->
						</div>
						<div class="relative">
							<input
								id="password"
								name="password"
								type={showPassword ? 'text' : 'password'}
								bind:value={password}
								required
								autocomplete="current-password"
								placeholder="••••••••••••"
								class="field w-full rounded-md py-3 pl-4 pr-12 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA]"
							/>
							<button
								type="button"
								onclick={() => (showPassword = !showPassword)}
								class="absolute right-2 top-1/2 flex h-8 w-8 -translate-y-1/2 items-center justify-center rounded-md text-[#A1A1AA] transition-colors hover:text-[#18181B]"
								aria-label={showPassword ? 'Hide password' : 'Show password'}
								aria-pressed={showPassword}
							>
								{@render icon(showPassword ? 'eye-off' : 'eye', 15)}
							</button>
						</div>
					</div>

					<!-- Primary action -->
					<button
						type="submit"
						disabled={loading}
						class="w-full rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14] disabled:opacity-60 disabled:cursor-not-allowed "
						
						
					>
						{loading ? "Signing in..." : "Sign in"}
					</button>
				</form>

				

			<!-- Register hint below the card -->
			<p class="mt-8 text-center text-sm font-light text-[#71717A]">
				Don’t have an account?
				<a
					href="/register"
					class="text-[#6D28D9] transition-colors hover:text-[#8B5CF6]"
				>
					Register
				</a>
			</p>
		</div>
	</main>

	<!-- ============ FOOTER ============ -->
	<footer class="border-t border-[#E4E4E7] bg-white px-6 py-8">
		<p class="text-center text-xs font-light text-[#A1A1AA]">
			Built quietly. Maintained openly.
		</p>
	</footer>
</div>

<style>
	.page {
		font-family: 'Inter', ui-sans-serif, system-ui, sans-serif;
		font-feature-settings: 'ss01' on, 'cv11' on;
	}

	/* ---- Daylight: morning sun through a tall window, above ---- */
	.daylight {
		background:
			radial-gradient(ellipse 90% 55% at 50% -18%, rgba(99, 102, 241, 0.1), transparent 62%),
			radial-gradient(ellipse 45% 30% at 50% -10%, rgba(139, 92, 246, 0.07), transparent 70%),
			linear-gradient(to bottom, #f6f6fa, #fafafa);
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

	/* ---- Form fields: quiet ink wells ---- */
	.field {
		background: #fafafa;
		border: 1px solid #e4e4e7;
		transition:
			border-color 150ms ease,
			background-color 150ms ease,
			box-shadow 150ms ease;
	}

	.field:hover {
		border-color: #d4d4d8;
	}

	.field:focus {
		outline: none;
		background: #ffffff;
		border-color: rgba(139, 92, 246, 0.45);
		box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.08);
	}

	/* ---- Lunar phase glyphs, drawn in ink (pure CSS) ---- */
	.crescent-lg {
		display: inline-block;
		height: 28px;
		width: 28px;
		border-radius: 9999px;
		box-shadow: inset -8px 4px 0 0 #6366f1;
	}
</style>