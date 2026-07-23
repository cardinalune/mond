import { api } from "./client";

export interface ValidationResponse {
	match: boolean;
	confidence: number;
	reasons: string[];

	anna_record: Record<string, any>;
	openlibrary_record: Record<string, any>;
}

export interface SubmitResponse {
	submission_id: string;
	status: string;
}

export async function validateMapping(
    md5: string,
    olid: string
): Promise<ValidationResponse> {

    return api<ValidationResponse>("/validate", {
        method: "POST",
        body: JSON.stringify({
            md5,
            olid,
        }),
    });
}

export async function submitMapping(payload: {
    md5: string;
    olid: string;
}): Promise<SubmitResponse> {

    return api<SubmitResponse>("/submit", {
        method: "POST",
        body: JSON.stringify(payload),
    });
}