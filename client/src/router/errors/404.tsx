import { createRoute } from "@tanstack/react-router";
import { publicRoute } from "..";
export const NotFoundRoute = createRoute({
    getParentRoute: () => publicRoute,
    path:"*",
    component: () => <h1>404 - Page Not Found</h1>
});
