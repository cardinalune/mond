import { api } from "./client";
import type {
	SubmitResponse,
    ValidationResponse,
    SubmissionHistoryItem,
    SubmissionStats,
} from "$lib/types/submit";

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

export async function getSubmissionHistory(): Promise<SubmissionHistoryItem[]> {
    return api<SubmissionHistoryItem[]>("/history", {
        method: "GET",
    });
}

export async function getSubmissionStats(): Promise<SubmissionStats> {
    return api<SubmissionStats>("/stats", {
        method: "GET",
    });
}