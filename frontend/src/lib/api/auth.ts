import { api } from "./client";
import type {
	SignupRequest,
	SignupResponse,
	LoginRequest,
	LoginResponse,
	CurrentUserResponse,
} from "$lib/types/auth";

export function signup(data: SignupRequest) {
	return api<SignupResponse>("/auth/signup", {
		method: "POST",
		body: JSON.stringify(data),
	});
}

export function login(data: LoginRequest) {
	return api<LoginResponse>("/auth/login", {
		method: "POST",
		body: JSON.stringify(data),
	});
}

export function getCurrentUser() {
	return api<CurrentUserResponse>("/auth/me", {
		method: "GET",
	});
}