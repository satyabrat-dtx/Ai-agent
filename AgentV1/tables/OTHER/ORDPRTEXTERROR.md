# DB2ADMIN.ORDPRTEXTERROR

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 27
- **Primary key**: `CUSTOMERSUPPLIERTYPE`, `LIFNR`, `BUKRS`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 129388

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 1 | `LIFNR` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `BUKRS` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 3 | `NAME1` | CHAR(100) |  |  |  |  |
| 4 | `KNANAME1` | CHAR(100) |  |  |  |  |
| 5 | `NAME2` | CHAR(100) |  |  |  |  |
| 6 | `NAME3` | CHAR(50) |  |  |  |  |
| 7 | `SORTL` | CHAR(60) |  |  |  |  |
| 8 | `LAND1` | CHAR(3) |  |  |  |  |
| 9 | `STCEG` | CHAR(30) |  |  |  |  |
| 10 | `REGIO` | CHAR(3) |  |  |  |  |
| 11 | `ORT01` | CHAR(100) |  |  |  |  |
| 12 | `PSTLZ` | CHAR(20) |  |  |  |  |
| 13 | `ORT02` | CHAR(100) |  |  |  |  |
| 14 | `TELF1` | CHAR(50) |  |  |  |  |
| 15 | `TELFX` | CHAR(50) |  |  |  |  |
| 16 | `KTOKK` | CHAR(3) |  |  |  |  |
| 17 | `STREET` | CHAR(100) |  |  |  |  |
| 18 | `LOCATION` | CHAR(100) |  |  |  |  |
| 19 | `ZWELS` | CHAR(3) |  |  |  |  |
| 20 | `PAFKT` | CHAR(100) |  |  |  |  |
| 21 | `EMAIL` | CHAR(100) |  |  |  |  |
| 22 | `STRSUPPL1` | CHAR(100) |  |  |  |  |
| 23 | `STRSUPPL2` | CHAR(100) |  |  |  |  |
| 24 | `STRSUPPL3` | CHAR(100) |  |  |  |  |
| 25 | `ERRORMESSAGE` | LONG VARCHAR |  |  |  |  |
| 26 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDPRTEXTERRORUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CUSTOMERSUPPLIERTYPE,
       t.LIFNR,
       t.BUKRS,
       t.NAME1,
       t.KNANAME1,
       t.NAME2,
       t.NAME3,
       t.SORTL,
       t.LAND1,
       t.STCEG,
       t.REGIO,
       t.ORT01
FROM   DB2ADMIN.ORDPRTEXTERROR t
FETCH FIRST 100 ROWS ONLY;
```
