
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

export interface SubmissionHistoryItem {
	id: string;
	md5: string;
	olid: string;

	title: string;

	status: "pending" | "approved" | "rejected";

	validation_score: number;

	submitted_at: string;
}

export interface SubmissionStats {
	pending: number;
	approved: number;
	rejected: number;
	total: number;
}