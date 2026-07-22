<script lang="ts">
	import "./layout.css";
	import favicon from "$lib/assets/favicon.svg";

	import { onMount } from "svelte";
	import { authLoading, loadCurrentUser } from "$lib/stores/auth";

	let { children } = $props();

	onMount(async () => {
		await loadCurrentUser();
	});
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

{#if $authLoading}
	Loading...
{:else}
	{@render children()}
{/if}