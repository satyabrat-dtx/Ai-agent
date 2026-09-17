# DB2ADMIN.PURCHASEORDERLINEIE

- **Module**: `PURCHASING` (high confidence — table name starts with 'PURCHASE')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `PURCHASEORDERCOMPANYCODE`, `PURCHASEORDERCOUNTERCODE`, `PURCHASEORDERCODE`, `ORDERLINE`, `ORDERSUBLINE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 134169

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TARIFFCODE` | CHAR(20) |  | FK | foreign_key |  |
| 1 | `PURCHASEORDERCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `PURORDERCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 3 | `PURCHASEORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `PURCHASEORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 5 | `ORDERLINE` | DECIMAL(7,0) | NOT NULL | PK | primary_key |  |
| 6 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `SCHEMETYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `TAXTEMPLATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 9 | `TAXTEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `CT3FORMNO` | CHAR(20) |  |  |  |  |
| 11 | `CT3DATE` | DATE |  |  |  |  |
| 12 | `BASICVALUE` | DECIMAL(18,5) |  |  |  |  |
| 13 | `GROSSVALUEWOHEADER` | DECIMAL(18,5) |  |  |  |  |
| 14 | `GROSSVALUEEXT` | DECIMAL(18,5) |  |  |  |  |
| 15 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 16 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 17 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 18 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 19 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 20 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `PLANTINVOICEDIVISIONCODE` | CHAR(3) |  |  |  |  |
| 23 | `PLANTINVOICECODE` | CHAR(15) |  |  |  |  |
| 24 | `INVOICELINENO` | DECIMAL(3,0) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_PURCHASEORDERCOMPANY` | `PURCHASEORDERCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PURCHASEORDERLINEIE.PURCHASEORDERCOMPANYCODE = COMPANY.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `PURCHASEORDERCOMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PURCHASEORDERLINEIE.PURCHASEORDERCOMPANYCODE = SCHEMETYPE.COMPANYCODE AND PURCHASEORDERLINEIE.SCHEMETYPECODE = SCHEMETYPE.CODE` |
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `PURCHASEORDERLINEIE.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PURCHASEORDERLINEIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TARIFFCODE,
       t.PURCHASEORDERCOMPANYCODE,
       t.PURORDERCOUNTERCOMPANYCODE,
       t.PURCHASEORDERCOUNTERCODE,
       t.PURCHASEORDERCODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.SCHEMETYPECODE,
       t.TAXTEMPLATETEMPLATETYPE,
       t.TAXTEMPLATECODE,
       t.CT3FORMNO,
       t.CT3DATE
FROM   DB2ADMIN.PURCHASEORDERLINEIE t
FETCH FIRST 100 ROWS ONLY;
```
