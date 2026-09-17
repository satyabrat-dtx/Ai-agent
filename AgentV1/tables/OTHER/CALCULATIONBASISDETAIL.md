# DB2ADMIN.CALCULATIONBASISDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `CLCBASISHEADERCOMPANYCODE`, `CALCULATIONBASISHEADERCODE`, `CLCBASISHDREFFECTIVEFROMDATE`, `LINEID`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123947

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CLCBASISHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `CALCULATIONBASISHEADERCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CLCBASISHDREFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINEID` | BIGINT | NOT NULL | PK | primary_key |  |
| 4 | `BASISCODECODE` | CHAR(3) |  |  |  |  |
| 5 | `ITAXCODE` | CHAR(3) |  |  |  |  |
| 6 | `SIGN` | INTEGER | NOT NULL |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CALCULATIONBASISHEADER_DETAIL` | `CLCBASISHEADERCOMPANYCODE`, `CALCULATIONBASISHEADERCODE`, `CLCBASISHDREFFECTIVEFROMDATE` | [`CALCULATIONBASISHEADER`](../OTHER/CALCULATIONBASISHEADER.md) | `COMPANYCODE`, `CODE`, `EFFECTIVEFROMDATE` | RESTRICT | `CALCULATIONBASISDETAIL.CLCBASISHEADERCOMPANYCODE = CALCULATIONBASISHEADER.COMPANYCODE AND CALCULATIONBASISDETAIL.CALCULATIONBASISHEADERCODE = CALCULATIONBASISHEADER.CODE AND CALCULATIONBASISDETAIL.CLCBASISHDREFFECTIVEFROMDATE = CALCULATIONBASISHEADER.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CALCULATIONBASISDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CLCBASISHEADERCOMPANYCODE,
       t.CALCULATIONBASISHEADERCODE,
       t.CLCBASISHDREFFECTIVEFROMDATE,
       t.LINEID,
       t.BASISCODECODE,
       t.ITAXCODE,
       t.SIGN,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.CALCULATIONBASISDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
