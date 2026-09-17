# DB2ADMIN.PROFTAXSLABDETAIL

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `PROFTAXSLABHEADERCOMPANYCODE`, `PROFTAXSLABHEADERDIVISIONCODE`, `PROFTAXSLABHEADERFACTORYCODE`, `PROFTAXSLABHEADERCODE`, `PROFTAXSLABHDREFFROMDATE`, `PROFTAXSLABHDREFFECTIVETODATE`, `SLABFROM`, `SLABTO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 159191

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `PROFTAXSLABHEADERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `PROFTAXSLABHEADERDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PROFTAXSLABHEADERFACTORYCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `PROFTAXSLABHEADERCODE` | CHAR(5) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `PROFTAXSLABHDREFFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `PROFTAXSLABHDREFFECTIVETODATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SLABFROM` | DECIMAL(11,2) | NOT NULL | PK | primary_key |  |
| 7 | `SLABTO` | DECIMAL(11,2) | NOT NULL | PK | primary_key |  |
| 8 | `PROFTAXAMOUNT` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 9 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 10 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 11 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 12 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 13 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 14 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `PROFTAXSLABHEADER_LINE` | `PROFTAXSLABHEADERCOMPANYCODE`, `PROFTAXSLABHEADERDIVISIONCODE`, `PROFTAXSLABHEADERFACTORYCODE`, `PROFTAXSLABHEADERCODE`, `PROFTAXSLABHDREFFROMDATE`, `PROFTAXSLABHDREFFECTIVETODATE` | [`PROFTAXSLABHEADER`](../OTHER/PROFTAXSLABHEADER.md) | `COMPANYCODE`, `DIVISIONCODE`, `FACTORYCODE`, `CODE`, `EFFECTIVEFROMDATE`, `EFFECTIVETODATE` | RESTRICT | `PROFTAXSLABDETAIL.PROFTAXSLABHEADERCOMPANYCODE = PROFTAXSLABHEADER.COMPANYCODE AND PROFTAXSLABDETAIL.PROFTAXSLABHEADERDIVISIONCODE = PROFTAXSLABHEADER.DIVISIONCODE AND PROFTAXSLABDETAIL.PROFTAXSLABHEADERFACTORYCODE = PROFTAXSLABHEADER.FACTORYCODE AND PROFTAXSLABDETAIL.PROFTAXSLABHEADERCODE = PROFTAXSLABHEADER.CODE AND PROFTAXSLABDETAIL.PROFTAXSLABHDREFFROMDATE = PROFTAXSLABHEADER.EFFECTIVEFROMDATE AND PROFTAXSLABDETAIL.PROFTAXSLABHDREFFECTIVETODATE = PROFTAXSLABHEADER.EFFECTIVETODATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PROFTAXSLABDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.PROFTAXSLABHEADERCOMPANYCODE,
       t.PROFTAXSLABHEADERDIVISIONCODE,
       t.PROFTAXSLABHEADERFACTORYCODE,
       t.PROFTAXSLABHEADERCODE,
       t.PROFTAXSLABHDREFFROMDATE,
       t.PROFTAXSLABHDREFFECTIVETODATE,
       t.SLABFROM,
       t.SLABTO,
       t.PROFTAXAMOUNT,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME
FROM   DB2ADMIN.PROFTAXSLABDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
