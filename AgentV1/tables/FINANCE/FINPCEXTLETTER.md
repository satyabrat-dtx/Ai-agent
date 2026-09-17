# DB2ADMIN.FINPCEXTLETTER

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `FINPACKINGCREDITCOMPANYCODE`, `FINPACKINGCREDITLETTERNO`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 177567

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `FINPACKINGCREDITCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `FINPACKINGCREDITLETTERNO` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `EXTENDEDDUEDATE` | DATE |  |  |  |  |
| 4 | `EXTENDEDINTERESTRATE` | DECIMAL(5,2) |  |  |  |  |
| 5 | `NARRATION` | CHAR(50) |  |  |  |  |
| 6 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 7 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 8 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 9 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 10 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 11 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `FINPACKINGCREDIT_PCEXTLETTER` | `FINPACKINGCREDITCOMPANYCODE`, `FINPACKINGCREDITLETTERNO` | [`FINPACKINGCREDIT`](../FINANCE/FINPACKINGCREDIT.md) | `COMPANYCODE`, `LETTERNO` | RESTRICT | `FINPCEXTLETTER.FINPACKINGCREDITCOMPANYCODE = FINPACKINGCREDIT.COMPANYCODE AND FINPCEXTLETTER.FINPACKINGCREDITLETTERNO = FINPACKINGCREDIT.LETTERNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINPCEXTLETTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.FINPACKINGCREDITCOMPANYCODE,
       t.FINPACKINGCREDITLETTERNO,
       t.LINENO,
       t.EXTENDEDDUEDATE,
       t.EXTENDEDINTERESTRATE,
       t.NARRATION,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC
FROM   DB2ADMIN.FINPCEXTLETTER t
FETCH FIRST 100 ROWS ONLY;
```
