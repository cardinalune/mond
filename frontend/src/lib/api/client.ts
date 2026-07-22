import { user } from "$lib/stores/auth";

const API_URL = import.meta.env.VITE_API_URL;

export async function api<T>(
	endpoint: string,
	options: RequestInit
): Promise<T> {
	const token = localStorage.getItem("access_token");

	const response = await fetch(`${API_URL}${endpoint}`, {
		...options,
		headers: {
			"Content-Type": "application/json",
			...(token
				? {
						Authorization: `Bearer ${token}`,
				  }
				: {}),
			...(options.headers ?? {}),
		},
	});

	const data = await response.json().catch(() => null);

	if (response.status === 401) {
	localStorage.removeItem("access_token");
	localStorage.removeItem("refresh_token");

	user.set(null);

	if (window.location.pathname !== "/login") {
		window.location.href = "/login";
	}

	throw new Error("Session expired.");
}
	if (!response.ok) {
		throw new Error(data?.detail ?? "Something went wrong.");
	}

	return data as T;
}