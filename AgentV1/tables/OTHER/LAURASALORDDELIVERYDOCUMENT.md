# DB2ADMIN.LAURASALORDDELIVERYDOCUMENT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 33
- **Primary key**: `COMPANYCODE`, `ORDERCOUNTERCODE`, `CODE`, `ORDERLINE`, `ORDERSUBLINE`, `COMPONENTORDERLINE`, `DELIVERYLINE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 18383

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `ORDERLINE` | DECIMAL(5,0) | NOT NULL | PK | primary_key |  |
| 4 | `ORDERSUBLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 5 | `COMPONENTORDERLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `DELIVERYLINE` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 7 | `PROGRESSSTATUS` | CHAR(2) |  |  |  |  |
| 8 | `ORDERTYPE` | CHAR(1) |  |  |  |  |
| 9 | `LINETEMPLATECODE` | CHAR(3) |  |  |  |  |
| 10 | `ITEMTYPEAFICODE` | CHAR(3) |  |  |  |  |
| 11 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 19 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `AMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 22 | `USEDAMOUNT` | DECIMAL(18,5) |  |  |  |  |
| 23 | `ONLYBYAMOUNT` | SMALLINT | NOT NULL |  |  |  |
| 24 | `SALESDOCUMENTCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 25 | `SALDOCPROVISIONALCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 26 | `SALESDOCUMENTPROVISIONALCODE` | CHAR(15) |  |  |  |  |
| 27 | `PREVIOUSCOUNTERCODE` | CHAR(8) |  |  |  |  |
| 28 | `PREVIOUSCODE` | CHAR(15) |  |  |  |  |
| 29 | `PREVIOUSORDERLINE` | DECIMAL(5,0) |  |  |  |  |
| 30 | `PREVIOUSORDERSUBLINE` | DECIMAL(3,0) |  |  |  |  |
| 31 | `PREVIOUSCOMPONENTORDERLINE` | DECIMAL(3,0) |  |  |  |  |
| 32 | `PREVIOUSDELIVERYLINE` | DECIMAL(3,0) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERCOUNTERCODE,
       t.CODE,
       t.ORDERLINE,
       t.ORDERSUBLINE,
       t.COMPONENTORDERLINE,
       t.DELIVERYLINE,
       t.PROGRESSSTATUS,
       t.ORDERTYPE,
       t.LINETEMPLATECODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01
FROM   DB2ADMIN.LAURASALORDDELIVERYDOCUMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
