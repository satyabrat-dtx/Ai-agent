# DB2ADMIN.TRAVELBOARDINGDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `TTRNDETAILTTRNCOMPANYCODE`, `TTRNDETAILTTRNSERIALNO`, `TTRNDETAILTTRNTRAVELTYPE`, `TTRNDETAILTOURSERIALNO`, `BOARDINGSERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 168942

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TTRNDETAILTTRNCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TTRNDETAILTTRNSERIALNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TTRNDETAILTTRNTRAVELTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TTRNDETAILTOURSERIALNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `BOARDINGSERIALNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `BOOKINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `AGENTICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 7 | `AGENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 8 | `BOARDINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `BOARDINGNAME` | CHAR(20) | NOT NULL |  |  |  |
| 10 | `BILLNO` | CHAR(15) | NOT NULL |  |  |  |
| 11 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 12 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 13 | `ITEM` | DECIMAL(10,0) |  |  |  |  |
| 14 | `SUMMARY` | CHAR(100) |  |  |  |  |
| 15 | `AMOUNT` | DECIMAL(11,2) |  |  |  |  |
| 16 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 17 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 18 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 19 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 20 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 21 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 22 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ICSENTITY_AGENT` | `TTRNDETAILTTRNCOMPANYCODE`, `AGENTICSTABLECODE`, `AGENTCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAVELBOARDINGDETAIL.TTRNDETAILTTRNCOMPANYCODE = ICSENTITY.COMPANYCODE AND TRAVELBOARDINGDETAIL.AGENTICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAVELBOARDINGDETAIL.AGENTCODE = ICSENTITY.CODE` |
| `TRAVELTRANSACTIONDETAIL_LINE2` | `TTRNDETAILTTRNCOMPANYCODE`, `TTRNDETAILTTRNSERIALNO`, `TTRNDETAILTTRNTRAVELTYPE`, `TTRNDETAILTOURSERIALNO` | [`TRAVELTRANSACTIONDETAIL`](../HR/TRAVELTRANSACTIONDETAIL.md) | `TRAVELTRANSACTIONCOMPANYCODE`, `TRAVELTRANSACTIONSERIALNO`, `TRAVELTRANSACTIONTRAVELTYPE`, `TOURSERIALNO` | RESTRICT | `TRAVELBOARDINGDETAIL.TTRNDETAILTTRNCOMPANYCODE = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONCOMPANYCODE AND TRAVELBOARDINGDETAIL.TTRNDETAILTTRNSERIALNO = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONSERIALNO AND TRAVELBOARDINGDETAIL.TTRNDETAILTTRNTRAVELTYPE = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONTRAVELTYPE AND TRAVELBOARDINGDETAIL.TTRNDETAILTOURSERIALNO = TRAVELTRANSACTIONDETAIL.TOURSERIALNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAVELBOARDINGDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TTRNDETAILTTRNCOMPANYCODE,
       t.TTRNDETAILTTRNSERIALNO,
       t.TTRNDETAILTTRNTRAVELTYPE,
       t.TTRNDETAILTOURSERIALNO,
       t.BOARDINGSERIALNO,
       t.BOOKINGTYPE,
       t.AGENTICSTABLECODE,
       t.AGENTCODE,
       t.BOARDINGTYPE,
       t.BOARDINGNAME,
       t.BILLNO,
       t.FROMDATE
FROM   DB2ADMIN.TRAVELBOARDINGDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
