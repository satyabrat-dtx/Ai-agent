# DB2ADMIN.TCSTAXDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `TCSTAXHEADERNUMBERID`, `TCSTAXHEADERCOMPANYCODE`, `TAXCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 222356

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TCSTAXHEADERNUMBERID` | DECIMAL(11,0) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TCSTAXHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TAXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `VALUE` | DECIMAL(18,5) |  |  |  |  |
| 4 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 5 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 6 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 7 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 8 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 9 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TCSTAXHEADER_DETAIL` | `TCSTAXHEADERNUMBERID`, `TCSTAXHEADERCOMPANYCODE` | [`TCSTAXHEADER`](../OTHER/TCSTAXHEADER.md) | `NUMBERID`, `COMPANYCODE` | RESTRICT | `TCSTAXDETAIL.TCSTAXHEADERNUMBERID = TCSTAXHEADER.NUMBERID AND TCSTAXDETAIL.TCSTAXHEADERCOMPANYCODE = TCSTAXHEADER.COMPANYCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TCSTAXDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TCSTAXHEADERNUMBERID,
       t.TCSTAXHEADERCOMPANYCODE,
       t.TAXCODE,
       t.VALUE,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC,
       t.LASTUPDATEDATETIMEUTC,
       t.ABSUNIQUEID
FROM   DB2ADMIN.TCSTAXDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
