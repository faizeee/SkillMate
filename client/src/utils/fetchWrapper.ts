type FetchOptions = RequestInit & {
  onStart?: () => void;
  onSuccess?: (data: any) => void;
  onError?: (error: string) => void;
  onFinish?: () => void;
};

export const fetchWrapper = async (url: string, options?: FetchOptions) => {
  try {
    options?.onStart?.();

    const res = await fetch(url, options);

    if (!res.ok) {
      throw new Error(`Fetch failed: ${res.status} ${res.statusText}`);
    }

    const data = await res.json();
    options?.onSuccess?.(data);
    return data;
  } catch (err: any) {
    const message = err?.message || "Something went wrong";
    options?.onError?.(message);
    return null;
  } finally {
    options?.onFinish?.();
  }
};
