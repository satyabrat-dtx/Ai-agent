# DB2ADMIN.DEFAULTREPORTSBYXML

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `UIXMLPATH`, `UIXMLNAME`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190176

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `UIXMLPATH` | VARCHAR(50) | NOT NULL | PK | primary_key |  |
| 1 | `UIXMLNAME` | VARCHAR(54) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `DEFAULTREPORTS` | VARCHAR(4000) |  |  |  |  |
| 4 | `PAUSEONPARAMETER` | SMALLINT | NOT NULL |  |  |  |
| 5 | `SENDBYMAIL` | SMALLINT | NOT NULL |  |  |  |
| 6 | `MAILADDRESS` | CHAR(120) |  |  |  |  |
| 7 | `MAILTEXT` | LONG VARCHAR |  |  |  |  |
| 8 | `ALLINONEMAIL` | SMALLINT | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `DEFAULTREPORTSBYXML_LINE` | [`DEFAULTREPORTSBYXMLLINE`](../OTHER/DEFAULTREPORTSBYXMLLINE.md) | `DEFAULTREPORTSBYXMLUIXMLPATH`, `DEFAULTREPORTSBYXMLUIXMLNAME`, `DEFAULTREPORTSBYXMLCODE` | `DEFAULTREPORTSBYXMLLINE.DEFAULTREPORTSBYXMLUIXMLPATH = DEFAULTREPORTSBYXML.UIXMLPATH AND DEFAULTREPORTSBYXMLLINE.DEFAULTREPORTSBYXMLUIXMLNAME = DEFAULTREPORTSBYXML.UIXMLNAME AND DEFAULTREPORTSBYXMLLINE.DEFAULTREPORTSBYXMLCODE = DEFAULTREPORTSBYXML.CODE` |

## Indexes

- `DEFAULTREPORTSBYXMLUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.UIXMLPATH,
       t.UIXMLNAME,
       t.CODE,
       t.DEFAULTREPORTS,
       t.PAUSEONPARAMETER,
       t.SENDBYMAIL,
       t.MAILADDRESS,
       t.MAILTEXT,
       t.ALLINONEMAIL,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.DEFAULTREPORTSBYXML t
FETCH FIRST 100 ROWS ONLY;
```
