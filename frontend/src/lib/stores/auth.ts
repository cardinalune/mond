import { writable } from "svelte/store";
import type { CurrentUserResponse } from "$lib/types/auth";
import { getCurrentUser } from "$lib/api/auth";
import { get } from "svelte/store";

export const user = writable<CurrentUserResponse | null>(null);

export const authLoading = writable(true);

export async function loadCurrentUser() {
	try {
		const currentUser = await getCurrentUser();

		user.set(currentUser);
	} catch {
		user.set(null);
	} finally {
		authLoading.set(false);
	}
}