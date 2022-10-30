create schema csvs;
create table csvs.UserInfo (
    UserID int,
    UserSex text,
    UserDevice text
);
copy csvs.UserInfo
from 'dataset/dataset/TR_UserInfo.csv'
delimiter ',' header csv;
