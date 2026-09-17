# DB2ADMIN.TRAVELOTHEREXPENSESDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `TTRNDETAILTTRNCOMPANYCODE`, `TTRNDETAILTTRNSERIALNO`, `TTRNDETAILTTRNTRAVELTYPE`, `TTRNDETAILTOURSERIALNO`, `OTHEREXPENSESERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169123

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TTRNDETAILTTRNCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TTRNDETAILTTRNSERIALNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TTRNDETAILTTRNTRAVELTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TTRNDETAILTOURSERIALNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `OTHEREXPENSESERIALNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `BOOKINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `AGENTICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 7 | `AGENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 8 | `BILLDATE` | DATE | NOT NULL |  |  |  |
| 9 | `BILLNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 10 | `ITEMNAME` | CHAR(10) | NOT NULL |  |  |  |
| 11 | `SUMMARYFIELD` | CHAR(100) |  |  |  |  |
| 12 | `AMOUNT` | DECIMAL(11,2) | NOT NULL |  |  |  |
| 13 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 14 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 15 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 16 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 17 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 18 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 19 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ICSENTITY_AGENT` | `TTRNDETAILTTRNCOMPANYCODE`, `AGENTICSTABLECODE`, `AGENTCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAVELOTHEREXPENSESDETAIL.TTRNDETAILTTRNCOMPANYCODE = ICSENTITY.COMPANYCODE AND TRAVELOTHEREXPENSESDETAIL.AGENTICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAVELOTHEREXPENSESDETAIL.AGENTCODE = ICSENTITY.CODE` |
| `TRAVELTRANSACTIONDETAIL_LINE3` | `TTRNDETAILTTRNCOMPANYCODE`, `TTRNDETAILTTRNSERIALNO`, `TTRNDETAILTTRNTRAVELTYPE`, `TTRNDETAILTOURSERIALNO` | [`TRAVELTRANSACTIONDETAIL`](../HR/TRAVELTRANSACTIONDETAIL.md) | `TRAVELTRANSACTIONCOMPANYCODE`, `TRAVELTRANSACTIONSERIALNO`, `TRAVELTRANSACTIONTRAVELTYPE`, `TOURSERIALNO` | RESTRICT | `TRAVELOTHEREXPENSESDETAIL.TTRNDETAILTTRNCOMPANYCODE = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONCOMPANYCODE AND TRAVELOTHEREXPENSESDETAIL.TTRNDETAILTTRNSERIALNO = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONSERIALNO AND TRAVELOTHEREXPENSESDETAIL.TTRNDETAILTTRNTRAVELTYPE = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONTRAVELTYPE AND TRAVELOTHEREXPENSESDETAIL.TTRNDETAILTOURSERIALNO = TRAVELTRANSACTIONDETAIL.TOURSERIALNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAVELOTHEREXPENSESDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TTRNDETAILTTRNCOMPANYCODE,
       t.TTRNDETAILTTRNSERIALNO,
       t.TTRNDETAILTTRNTRAVELTYPE,
       t.TTRNDETAILTOURSERIALNO,
       t.OTHEREXPENSESERIALNO,
       t.BOOKINGTYPE,
       t.AGENTICSTABLECODE,
       t.AGENTCODE,
       t.BILLDATE,
       t.BILLNUMBER,
       t.ITEMNAME,
       t.SUMMARYFIELD
FROM   DB2ADMIN.TRAVELOTHEREXPENSESDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
