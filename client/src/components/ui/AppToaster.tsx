import { Toaster } from "sonner";

export default function AppToaster (){
    return <Toaster
     theme="system"
      richColors
      position="top-right"
      closeButton
      toastOptions={{
        duration: 3000,
      }}
    />
}
