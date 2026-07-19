svelte
<!-- src/routes/register/+page.svelte -->
<script lang="ts">
	// Lucide icon path data, inlined — no icon package required.
	const iconPaths: Record<string, string> = {
		eye: '<path d="M2.062 12.348a1 1 0 0 1 0-.696 10.75 10.75 0 0 1 19.876 0 1 1 0 0 1 0 .696 10.75 10.75 0 0 1-19.876 0"/><circle cx="12" cy="12" r="3"/>',
		'eye-off':
			'<path d="M10.733 5.076a10.744 10.744 0 0 1 11.205 6.575 1 1 0 0 1 0 .696 10.747 10.747 0 0 1-1.444 2.49"/><path d="M14.084 14.158a3 3 0 0 1-4.242-4.242"/><path d="M17.479 17.499a10.75 10.75 0 0 1-15.417-5.151 1 1 0 0 1 0-.696 10.75 10.75 0 0 1 4.446-5.143"/><path d="m2 2 20 20"/>',
		'arrow-left': '<path d="m12 19-7-7 7-7"/><path d="M19 12H5"/>'
	};

	let username = $state('');
	let email = $state('');
	let password = $state('');
	let confirmPassword = $state('');
	let showPassword = $state(false);
	let showConfirmPassword = $state(false);

	// Validation error placeholders. Populate from a form action in production.
	// Example: errors.email = 'Email is required.';
	const errors: Record<'username' | 'email' | 'password' | 'confirmPassword', string> = {
		username: '',
		email: '',
		password: '',
		confirmPassword: ''
	};

	function handleSubmit(event: SubmitEvent) {
		event.preventDefault();
		// Wire to a form action in production.
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

{#snippet fieldError(id: string, message: string)}
	{#if message}
		<p id={id} class="mt-2 text-xs font-light text-[#DC2626]">
			{message}
		</p>
	{/if}
{/snippet}

<svelte:head>
	<title>Create account — Mond</title>
	<meta
		name="description"
		content="Create your Mond account to contribute verified mappings between Anna’s Archive and Open Library."
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
				href="/login"
				class="rounded-md border border-[#E4E4E7] bg-white px-4 py-2 text-sm text-[#18181B] shadow-sm transition-colors hover:border-[#8B5CF6]/40 hover:bg-[#8B5CF6]/[0.05]"
			>
				Sign in
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

			<div class="paper rounded-lg p-8 sm:p-10">
				<p class="text-[11px] tracking-[0.35em] uppercase text-[#A1A1AA]">
					Welcome
				</p>
				<h1 class="mt-4 text-3xl font-extralight tracking-tight text-[#18181B]">
					Create account
				</h1>
				<p class="mt-3 text-sm font-light leading-relaxed text-[#52525B]">
					Create your Mond account to contribute verified mappings between
					Anna’s Archive and Open Library.
				</p>

				<form class="mt-10 space-y-6" onsubmit={handleSubmit} novalidate>
					<!-- Username -->
					<div>
						<label
							for="username"
							class="mb-2.5 block text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							Username
						</label>
						<input
							id="username"
							name="username"
							type="text"
							bind:value={username}
							required
							autocomplete="username"
							placeholder="lena"
							aria-describedby="username-error"
							aria-invalid={errors.username ? 'true' : undefined}
							class="field w-full rounded-md px-4 py-3 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA]"
						/>
						{@render fieldError('username-error', errors.username)}
					</div>

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
							aria-describedby="email-error"
							aria-invalid={errors.email ? 'true' : undefined}
							class="field w-full rounded-md px-4 py-3 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA]"
						/>
						{@render fieldError('email-error', errors.email)}
					</div>

					<!-- Password -->
					<div>
						<label
							for="password"
							class="mb-2.5 block text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							Password
						</label>
						<div class="relative">
							<input
								id="password"
								name="password"
								type={showPassword ? 'text' : 'password'}
								bind:value={password}
								required
								autocomplete="new-password"
								placeholder="••••••••••••"
								aria-describedby="password-error"
								aria-invalid={errors.password ? 'true' : undefined}
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
						{@render fieldError('password-error', errors.password)}
					</div>

					<!-- Confirm Password -->
					<div>
						<label
							for="confirm-password"
							class="mb-2.5 block text-[11px] tracking-[0.25em] uppercase text-[#71717A]"
						>
							Confirm password
						</label>
						<div class="relative">
							<input
								id="confirm-password"
								name="confirmPassword"
								type={showConfirmPassword ? 'text' : 'password'}
								bind:value={confirmPassword}
								required
								autocomplete="new-password"
								placeholder="••••••••••••"
								aria-describedby="confirm-password-error"
								aria-invalid={errors.confirmPassword ? 'true' : undefined}
								class="field w-full rounded-md py-3 pl-4 pr-12 text-sm font-light text-[#18181B] placeholder:text-[#A1A1AA]"
							/>
							<button
								type="button"
								onclick={() => (showConfirmPassword = !showConfirmPassword)}
								class="absolute right-2 top-1/2 flex h-8 w-8 -translate-y-1/2 items-center justify-center rounded-md text-[#A1A1AA] transition-colors hover:text-[#18181B]"
								aria-label={showConfirmPassword ? 'Hide password' : 'Show password'}
								aria-pressed={showConfirmPassword}
							>
								{@render icon(showConfirmPassword ? 'eye-off' : 'eye', 15)}
							</button>
						</div>
						{@render fieldError('confirm-password-error', errors.confirmPassword)}
					</div>

					<!-- Primary action -->
					<button
						type="submit"
						class="w-full rounded-md border border-[#8B5CF6]/30 bg-[#8B5CF6]/[0.07] px-6 py-3 text-sm text-[#6D28D9] transition-colors hover:bg-[#8B5CF6]/[0.14]"
					>
						Create account
					</button>
				</form>
			</div>

			<!-- Sign-in hint below the card -->
			<p class="mt-8 text-center text-sm font-light text-[#71717A]">
				Already have an account?
				<a
					href="/login"
					class="text-[#6D28D9] transition-colors hover:text-[#8B5CF6]"
				>
					Sign in
				</a>
			</p>
		</div>
	</main>

	<!-- ============ FOOTER ============ -->
	<footer class="border-t border-[#E4E4E7] bg-white px-6 py-8">
		<p class="text-center text-xs font-light text-[#A1A1AA]">
			Mond preserves knowledge through careful human verification.
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

	.field[aria-invalid='true'] {
		border-color: rgba(239, 68, 68, 0.45);
	}

	.field[aria-invalid='true']:focus {
		box-shadow: 0 0 0 3px rgba(239, 68, 68, 0.08);
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