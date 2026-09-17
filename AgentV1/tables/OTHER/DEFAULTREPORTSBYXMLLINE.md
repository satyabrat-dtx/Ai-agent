# DB2ADMIN.DEFAULTREPORTSBYXMLLINE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `DEFAULTREPORTSBYXMLUIXMLPATH`, `DEFAULTREPORTSBYXMLUIXMLNAME`, `DEFAULTREPORTSBYXMLCODE`, `USERUSERID`, `COMPANYCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 190223

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `DEFAULTREPORTSBYXMLUIXMLPATH` | VARCHAR(50) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `DEFAULTREPORTSBYXMLUIXMLNAME` | VARCHAR(54) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `DEFAULTREPORTSBYXMLCODE` | CHAR(10) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `USERUSERID` | CHAR(50) | NOT NULL | PK | primary_key |  |
| 4 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 5 | `EXCLUDE` | SMALLINT | NOT NULL |  |  |  |
| 6 | `DEFAULTREPORTS` | VARCHAR(4000) |  |  |  |  |
| 7 | `PAUSEONPARAMETER` | SMALLINT | NOT NULL |  |  |  |
| 8 | `SENDBYMAIL` | SMALLINT | NOT NULL |  |  |  |
| 9 | `MAILADDRESS` | CHAR(120) |  |  |  |  |
| 10 | `MAILTEXT` | LONG VARCHAR |  |  |  |  |
| 11 | `ALLINONEMAIL` | SMALLINT | NOT NULL |  |  |  |
| 12 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 13 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 14 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 15 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 16 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 17 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `DEFAULTREPORTSBYXML_LINE` | `DEFAULTREPORTSBYXMLUIXMLPATH`, `DEFAULTREPORTSBYXMLUIXMLNAME`, `DEFAULTREPORTSBYXMLCODE` | [`DEFAULTREPORTSBYXML`](../OTHER/DEFAULTREPORTSBYXML.md) | `UIXMLPATH`, `UIXMLNAME`, `CODE` | RESTRICT | `DEFAULTREPORTSBYXMLLINE.DEFAULTREPORTSBYXMLUIXMLPATH = DEFAULTREPORTSBYXML.UIXMLPATH AND DEFAULTREPORTSBYXMLLINE.DEFAULTREPORTSBYXMLUIXMLNAME = DEFAULTREPORTSBYXML.UIXMLNAME AND DEFAULTREPORTSBYXMLLINE.DEFAULTREPORTSBYXMLCODE = DEFAULTREPORTSBYXML.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `DEFAULTREPORTSBYXMLLINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.DEFAULTREPORTSBYXMLUIXMLPATH,
       t.DEFAULTREPORTSBYXMLUIXMLNAME,
       t.DEFAULTREPORTSBYXMLCODE,
       t.USERUSERID,
       t.COMPANYCODE,
       t.EXCLUDE,
       t.DEFAULTREPORTS,
       t.PAUSEONPARAMETER,
       t.SENDBYMAIL,
       t.MAILADDRESS,
       t.MAILTEXT,
       t.ALLINONEMAIL
FROM   DB2ADMIN.DEFAULTREPORTSBYXMLLINE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
