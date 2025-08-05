export interface LoginCredentials {
  username: string;
  password: string;
}

export type User = {
  username: string;
  id: string | Number;
  role: {
    id: string | Number;
    title: string;
    description: string;
  };
  role_name: string;
};

export type AuthResponse = {
  access_token: string;
  token_type: string;
  user: User;
};
