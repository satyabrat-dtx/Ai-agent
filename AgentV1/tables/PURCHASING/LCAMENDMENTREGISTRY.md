# DB2ADMIN.LCAMENDMENTREGISTRY

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `LCDETAILCOMPANYCODE`, `LCDETAILLCNO`, `LCDETAILLCDATE`, `LCAMENDMENTNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 139524

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `LCDETAILCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `LCDETAILLCNO` | CHAR(35) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LCDETAILLCDATE` | DATE | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LCAMENDMENTNO` | DECIMAL(2,0) | NOT NULL | PK | primary_key |  |
| 4 | `LCVALUE` | DECIMAL(18,5) |  |  |  |  |
| 5 | `AMENDMENTDATE` | DATE |  |  |  |  |
| 6 | `REMARKS` | VARCHAR(100) |  |  |  |  |
| 7 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 8 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 9 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 10 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 11 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 12 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 14 | `AMEDNMENTQUANTITY` | DECIMAL(18,5) |  |  |  |  |
| 15 | `AMENDMENTAMT` | DECIMAL(18,5) |  |  |  |  |
| 16 | `AMENDMENTGROSSAMT` | DECIMAL(18,5) |  |  |  |  |
| 17 | `NETQUANTITY` | DECIMAL(15,5) |  |  |  |  |
| 18 | `NETAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 19 | `TOTALGROSSAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 20 | `EXTENDEDSHIPMENTDATE` | DATE |  |  |  |  |
| 21 | `EXTENDEDEXPIRYDATE` | DATE |  |  |  |  |
| 22 | `UGGUSERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `UGGCODE` | CHAR(10) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `LCDETAIL_AMMENDDETAIL` | `LCDETAILCOMPANYCODE`, `LCDETAILLCNO`, `LCDETAILLCDATE` | [`LCDETAIL`](../PURCHASING/LCDETAIL.md) | `COMPANYCODE`, `LCNO`, `LCDATE` | RESTRICT | `LCAMENDMENTREGISTRY.LCDETAILCOMPANYCODE = LCDETAIL.COMPANYCODE AND LCAMENDMENTREGISTRY.LCDETAILLCNO = LCDETAIL.LCNO AND LCAMENDMENTREGISTRY.LCDETAILLCDATE = LCDETAIL.LCDATE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `LCAMENDMENTREGISTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.LCDETAILCOMPANYCODE,
       t.LCDETAILLCNO,
       t.LCDETAILLCDATE,
       t.LCAMENDMENTNO,
       t.LCVALUE,
       t.AMENDMENTDATE,
       t.REMARKS,
       t.CREATIONDATETIME,
       t.CREATIONUSER,
       t.LASTUPDATEDATETIME,
       t.LASTUPDATEUSER,
       t.CREATIONDATETIMEUTC
FROM   DB2ADMIN.LCAMENDMENTREGISTRY t
FETCH FIRST 100 ROWS ONLY;
```
