# DB2ADMIN.BUSINESSPARTNERCONTACTBOOK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `BUSINESSPARTNERNUMBERID`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 9345

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `BUSINESSPARTNERNUMBERID` | DECIMAL(8,0) | NOT NULL | PK | primary_key |  |
| 1 | `CODE` | CHAR(8) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `PERSONTOCONTACT` | CHAR(50) | NOT NULL |  |  |  |
| 3 | `ROLEINTHECOMPANY` | CHAR(50) |  |  |  |  |
| 4 | `PHONENUMBER` | CHAR(20) |  |  |  |  |
| 5 | `FAXNUMBER` | CHAR(20) |  |  |  |  |
| 6 | `EMAILADDRESS` | CHAR(50) |  |  |  |  |
| 7 | `BOOKLINE01` | CHAR(50) |  |  |  |  |
| 8 | `BOOKLINE02` | CHAR(50) |  |  |  |  |
| 9 | `BOOKLINE03` | CHAR(50) |  |  |  |  |
| 10 | `BOOKLINE04` | CHAR(50) |  |  |  |  |
| 11 | `BOOKLINE05` | CHAR(50) |  |  |  |  |
| 12 | `COUNTRYCODE` | CHAR(3) |  |  |  |  |
| 13 | `ADDRESSLINE1` | CHAR(50) |  |  |  |  |
| 14 | `ADDRESSLINE2` | CHAR(50) |  |  |  |  |
| 15 | `ADDRESSLINE3` | CHAR(50) |  |  |  |  |
| 16 | `POSTALCODE` | CHAR(20) |  |  |  |  |
| 17 | `TOWN` | CHAR(50) |  |  |  |  |
| 18 | `DISTRICT` | CHAR(50) |  |  |  |  |
| 19 | `TRANSPORTZONECODE` | CHAR(3) |  |  |  |  |
| 20 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 21 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 22 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 23 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.BUSINESSPARTNERNUMBERID,
       t.CODE,
       t.PERSONTOCONTACT,
       t.ROLEINTHECOMPANY,
       t.PHONENUMBER,
       t.FAXNUMBER,
       t.EMAILADDRESS,
       t.BOOKLINE01,
       t.BOOKLINE02,
       t.BOOKLINE03,
       t.BOOKLINE04,
       t.BOOKLINE05
FROM   DB2ADMIN.BUSINESSPARTNERCONTACTBOOK t
FETCH FIRST 100 ROWS ONLY;
```
