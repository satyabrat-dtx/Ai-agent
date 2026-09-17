# DB2ADMIN.TRAVELRULEDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `TRAVELRULECOMPANYCODE`, `TRAVELRULEITEMTYPE`, `TRLEMPLOYEEGRADEICSTABLECODE`, `TRAVELRULEEMPLOYEEGRADECODE`, `TRAVELRULEEFFECTIVEFROMDATE`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 161943

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TRAVELRULECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TRAVELRULEITEMTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TRLEMPLOYEEGRADEICSTABLECODE` | CHAR(4) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TRAVELRULEEMPLOYEEGRADECODE` | CHAR(6) | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `TRAVELRULEEFFECTIVEFROMDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SERIALNO` | BIGINT | NOT NULL | PK | primary_key |  |
| 6 | `CITYCLASSCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `TRAVELMODEICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 8 | `TRAVELMODECODE` | CHAR(6) |  | FK | foreign_key |  |
| 9 | `MAXLIMIT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 10 | `REMARKS` | CHAR(25) |  |  |  |  |
| 11 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 12 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 13 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 14 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 15 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 16 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `CITY_CITYCLASS` | `CITYCLASSCODE` | [`CITY`](../HR/CITY.md) | `CODE` | RESTRICT | `TRAVELRULEDETAIL.CITYCLASSCODE = CITY.CODE` |
| `ICSENTITY_TRAVELMODE` | `TRAVELRULECOMPANYCODE`, `TRAVELMODEICSTABLECODE`, `TRAVELMODECODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAVELRULEDETAIL.TRAVELRULECOMPANYCODE = ICSENTITY.COMPANYCODE AND TRAVELRULEDETAIL.TRAVELMODEICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAVELRULEDETAIL.TRAVELMODECODE = ICSENTITY.CODE` |
| `TRAVELRULE_LINE` | `TRAVELRULECOMPANYCODE`, `TRAVELRULEITEMTYPE`, `TRLEMPLOYEEGRADEICSTABLECODE`, `TRAVELRULEEMPLOYEEGRADECODE`, `TRAVELRULEEFFECTIVEFROMDATE` | [`TRAVELRULE`](../HR/TRAVELRULE.md) | `COMPANYCODE`, `ITEMTYPE`, `EMPLOYEEGRADEICSTABLECODE`, `EMPLOYEEGRADECODE`, `EFFECTIVEFROMDATE` | RESTRICT | `TRAVELRULEDETAIL.TRAVELRULECOMPANYCODE = TRAVELRULE.COMPANYCODE AND TRAVELRULEDETAIL.TRAVELRULEITEMTYPE = TRAVELRULE.ITEMTYPE AND TRAVELRULEDETAIL.TRLEMPLOYEEGRADEICSTABLECODE = TRAVELRULE.EMPLOYEEGRADEICSTABLECODE AND TRAVELRULEDETAIL.TRAVELRULEEMPLOYEEGRADECODE = TRAVELRULE.EMPLOYEEGRADECODE AND TRAVELRULEDETAIL.TRAVELRULEEFFECTIVEFROMDATE = TRAVELRULE.EFFECTIVEFROMDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAVELRULEDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TRAVELRULECOMPANYCODE,
       t.TRAVELRULEITEMTYPE,
       t.TRLEMPLOYEEGRADEICSTABLECODE,
       t.TRAVELRULEEMPLOYEEGRADECODE,
       t.TRAVELRULEEFFECTIVEFROMDATE,
       t.SERIALNO,
       t.CITYCLASSCODE,
       t.TRAVELMODEICSTABLECODE,
       t.TRAVELMODECODE,
       t.MAXLIMIT,
       t.REMARKS,
       t.CREATIONDATETIME
FROM   DB2ADMIN.TRAVELRULEDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
