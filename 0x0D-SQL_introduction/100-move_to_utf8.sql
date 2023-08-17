-- Convert `hbtn_0c_0` db and table `first_table`
-- as well as column `name` to utfmb4 encoding.
USE hbtn_0c_0;
ALTER DATABASE
      hbtn_0c_0
      CHARACTER SET = utf8mb4
      COLLATE = utf8mb4_unicode_ci;
ALTER TABLE
      first_table
      CONVERT TO CHARACTER SET utf8mb4
      COLLATE utf8mb4_unicode_ci;
ALTER TABLE
      first_table
      CHANGE `name` `name` VARCHAR(256)
      CHARACTER SET utf8mb4
      COLLATE utf8mb4_unicode_ci;
