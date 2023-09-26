import { AuthPage, ThemedTitleV2 } from "@refinedev/mui";

export const Login = () => {
  return (
    <AuthPage
      type="login"
      title={
        <ThemedTitleV2
          collapsed={false}
          text="Project Home"
        />
      }
      formProps={{
        defaultValues: { email: "demo@refine.dev", password: "demodemo" },
      }}
    />
  );
};
