-- this file was manually created
INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Maureen Msaghu', 'maureenmwagoti@gmail.com', 'maureenmsaghu' ,'MOCK'),
  ('Andrew Bayko', 'bayko@exampro.co', 'bayko' ,'MOCK'),
  ('Honey Mwaghoti', 'maureenmwagoti+1@gmail.com', 'honeymwaghoti' ,'MOCK');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'Maureen Msaghu' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )