type ApiErrorDetails = string | { msg: string }[] | { message: string };
interface ApiErrorResponse {
  detail: ApiErrorDetails;
}

export const handleApiError = async (response: Response): Promise<never> => {
  const errData: ApiErrorResponse = await response.json();
  let errMessage = "Something went wrong";
  if (typeof errData.detail === "string") {
    errMessage = errData.detail;
  } else if (Array.isArray(errData.detail)) {
    // This checks if the array contains objects with a 'msg' property
    const hasMsg = (e: any): e is { msg: string } => typeof e.msg === "string";
    errMessage = errData.detail
      .filter(hasMsg)
      .map((e) => e.msg)
      .join(", ");
  } else if (
    typeof errData.detail === "object" &&
    "message" in errData.detail
  ) {
    errMessage = errData.detail.message;
  }

  // We throw an Error with the formatted message
  // so the calling function's catch block can handle it.
  throw new Error(errMessage);
};
