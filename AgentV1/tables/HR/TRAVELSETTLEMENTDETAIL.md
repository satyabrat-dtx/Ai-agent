# DB2ADMIN.TRAVELSETTLEMENTDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 22
- **Primary key**: `TRAVELSETTLEMENTCOMPANYCODE`, `TRAVELSETTLEMENTSETTLEMENTNO`, `TSTTOURNUMBERTOURNUMBER`, `SERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169237

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TRAVELSETTLEMENTCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TRAVELSETTLEMENTSETTLEMENTNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TSTTOURNUMBERTOURNUMBER` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 4 | `SERIALNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `EXPENCEITEM` | INTEGER | NOT NULL |  |  |  |
| 6 | `BILLNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 7 | `FLAGSPENT` | INTEGER | NOT NULL |  |  |  |
| 8 | `AMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 9 | `CANCELLATION` | SMALLINT | NOT NULL |  |  |  |
| 10 | `CANCELLATIONAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 11 | `REASONFORCANCEL` | CHAR(100) |  |  |  |  |
| 12 | `CREDIT` | DECIMAL(13,0) |  |  |  |  |
| 13 | `CANCELLATIONCHARGE` | DECIMAL(17,2) |  |  |  |  |
| 14 | `OTHERCHARGE` | DECIMAL(17,2) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `TRAVELSETTLEMENT_LINE` | `TRAVELSETTLEMENTCOMPANYCODE`, `TRAVELSETTLEMENTSETTLEMENTNO`, `TSTTOURNUMBERTOURNUMBER` | [`TRAVELSETTLEMENT`](../HR/TRAVELSETTLEMENT.md) | `COMPANYCODE`, `SETTLEMENTNO`, `TOURNUMBERTOURNUMBER` | RESTRICT | `TRAVELSETTLEMENTDETAIL.TRAVELSETTLEMENTCOMPANYCODE = TRAVELSETTLEMENT.COMPANYCODE AND TRAVELSETTLEMENTDETAIL.TRAVELSETTLEMENTSETTLEMENTNO = TRAVELSETTLEMENT.SETTLEMENTNO AND TRAVELSETTLEMENTDETAIL.TSTTOURNUMBERTOURNUMBER = TRAVELSETTLEMENT.TOURNUMBERTOURNUMBER` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAVELSETTLEMENTDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TRAVELSETTLEMENTCOMPANYCODE,
       t.TRAVELSETTLEMENTSETTLEMENTNO,
       t.TSTTOURNUMBERTOURNUMBER,
       t.CHOOSE,
       t.SERIALNO,
       t.EXPENCEITEM,
       t.BILLNUMBER,
       t.FLAGSPENT,
       t.AMOUNT,
       t.CANCELLATION,
       t.CANCELLATIONAMOUNT,
       t.REASONFORCANCEL
FROM   DB2ADMIN.TRAVELSETTLEMENTDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
