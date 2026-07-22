export interface SignupRequest {
	username: string;
	email: string;
	password: string;
}

export interface SignupResponse {
	message: string;
	user_id: string;
}

export interface LoginRequest {
	email: string;
	password: string;
}

export interface LoginResponse {
	access_token: string;
	refresh_token: string;
	expires_in: number;
	token_type: string;

	role: string;
}

export interface CurrentUserResponse {
	id: string;
	username: string;
	email: string;
	role: "user" | "moderator" | "admin";
}