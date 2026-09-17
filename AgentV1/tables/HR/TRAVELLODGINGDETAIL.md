# DB2ADMIN.TRAVELLODGINGDETAIL

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 23
- **Primary key**: `TTRNDETAILTTRNCOMPANYCODE`, `TTRNDETAILTTRNSERIALNO`, `TTRNDETAILTTRNTRAVELTYPE`, `TTRNDETAILTOURSERIALNO`, `LODGINGSERIALNO`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169067

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TTRNDETAILTTRNCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `TTRNDETAILTTRNSERIALNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `TTRNDETAILTTRNTRAVELTYPE` | INTEGER | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `TTRNDETAILTOURSERIALNO` | BIGINT | NOT NULL | PK FK | primary_key foreign_key |  |
| 4 | `LODGINGSERIALNO` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 5 | `BOOKINGTYPE` | INTEGER | NOT NULL |  |  |  |
| 6 | `AGENTICSTABLECODE` | CHAR(4) |  | FK | foreign_key |  |
| 7 | `AGENTCODE` | CHAR(6) |  | FK | foreign_key |  |
| 8 | `ACCTYPE` | INTEGER | NOT NULL |  |  |  |
| 9 | `ACCNAME` | CHAR(20) | NOT NULL |  |  |  |
| 10 | `ACCCONTACTNO` | DECIMAL(10,0) |  |  |  |  |
| 11 | `FROMDATE` | DATE | NOT NULL |  |  | Inclusive start of a validity period. |
| 12 | `TODATE` | DATE | NOT NULL |  |  | End of a validity period. |
| 13 | `BILLNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 14 | `SUMMARY` | CHAR(100) |  |  |  |  |
| 15 | `AMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
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
| `ICSENTITY_AGENT` | `TTRNDETAILTTRNCOMPANYCODE`, `AGENTICSTABLECODE`, `AGENTCODE` | [`ICSENTITY`](../CORE_MASTER/ICSENTITY.md) | `COMPANYCODE`, `ICSTABLECODE`, `CODE` | RESTRICT | `TRAVELLODGINGDETAIL.TTRNDETAILTTRNCOMPANYCODE = ICSENTITY.COMPANYCODE AND TRAVELLODGINGDETAIL.AGENTICSTABLECODE = ICSENTITY.ICSTABLECODE AND TRAVELLODGINGDETAIL.AGENTCODE = ICSENTITY.CODE` |
| `TRAVELTRANSACTIONDETAIL_LINE1` | `TTRNDETAILTTRNCOMPANYCODE`, `TTRNDETAILTTRNSERIALNO`, `TTRNDETAILTTRNTRAVELTYPE`, `TTRNDETAILTOURSERIALNO` | [`TRAVELTRANSACTIONDETAIL`](../HR/TRAVELTRANSACTIONDETAIL.md) | `TRAVELTRANSACTIONCOMPANYCODE`, `TRAVELTRANSACTIONSERIALNO`, `TRAVELTRANSACTIONTRAVELTYPE`, `TOURSERIALNO` | RESTRICT | `TRAVELLODGINGDETAIL.TTRNDETAILTTRNCOMPANYCODE = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONCOMPANYCODE AND TRAVELLODGINGDETAIL.TTRNDETAILTTRNSERIALNO = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONSERIALNO AND TRAVELLODGINGDETAIL.TTRNDETAILTTRNTRAVELTYPE = TRAVELTRANSACTIONDETAIL.TRAVELTRANSACTIONTRAVELTYPE AND TRAVELLODGINGDETAIL.TTRNDETAILTOURSERIALNO = TRAVELTRANSACTIONDETAIL.TOURSERIALNO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `TRAVELLODGINGDETAILUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TTRNDETAILTTRNCOMPANYCODE,
       t.TTRNDETAILTTRNSERIALNO,
       t.TTRNDETAILTTRNTRAVELTYPE,
       t.TTRNDETAILTOURSERIALNO,
       t.LODGINGSERIALNO,
       t.BOOKINGTYPE,
       t.AGENTICSTABLECODE,
       t.AGENTCODE,
       t.ACCTYPE,
       t.ACCNAME,
       t.ACCCONTACTNO,
       t.FROMDATE
FROM   DB2ADMIN.TRAVELLODGINGDETAIL t
FETCH FIRST 100 ROWS ONLY;
```
