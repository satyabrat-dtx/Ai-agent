# DB2ADMIN.MRNREGISTER

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `LINENO`, `MRNPREFIXCODE`, `MRNNO`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 133744

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `TAXCODE1` | CHAR(3) |  |  |  |  |
| 1 | `TAXCODE2` | CHAR(3) |  |  |  |  |
| 2 | `TAXCODE3` | CHAR(3) |  |  |  |  |
| 3 | `TAXCODE4` | CHAR(3) |  |  |  |  |
| 4 | `TAXCODE5` | CHAR(3) |  |  |  |  |
| 5 | `OTHERCODES` | CHAR(3) |  |  |  |  |
| 6 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 7 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key | Division within a company; second-level organisational discriminator. |
| 8 | `SUBCODE01` | CHAR(20) |  |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(20) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(20) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(20) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(20) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(20) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(20) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(20) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(20) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(20) |  |  | generic_classification_code |  |
| 18 | `MRNPREFIXCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 19 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 20 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 21 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 22 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 23 | `MRNNO` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 24 | `MRNDATE` | DATE |  |  |  |  |
| 25 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 26 | `MRNFLAG` | INTEGER | NOT NULL |  |  |  |
| 27 | `VALUE1` | DECIMAL(18,5) |  |  |  |  |
| 28 | `VALUE2` | DECIMAL(18,5) |  |  |  |  |
| 29 | `VALUE3` | DECIMAL(18,5) |  |  |  |  |
| 30 | `VALUE4` | DECIMAL(18,5) |  |  |  |  |
| 31 | `VALUE5` | DECIMAL(18,5) |  |  |  |  |
| 32 | `VALUEOTHERS` | DECIMAL(18,5) |  |  |  |  |
| 33 | `UMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 34 | `QTY` | DECIMAL(15,5) |  |  |  |  |
| 35 | `NETVALUE` | DECIMAL(18,5) |  |  |  |  |
| 36 | `MRNLINEGROSSVALUE` | DECIMAL(18,5) |  |  |  |  |
| 37 | `CURRENCYCODE` | CHAR(4) |  | FK | foreign_key |  |
| 38 | `ITEMDESC` | VARCHAR(200) |  |  |  |  |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `MRNREGISTER.COMPANYCODE = COMPANY.CODE` |
| `CURRENCY_CURRENCY` | `CURRENCYCODE` | [`CURRENCY`](../CORE_MASTER/CURRENCY.md) | `CODE` | RESTRICT | `MRNREGISTER.CURRENCYCODE = CURRENCY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MRNREGISTER.COMPANYCODE = DIVISION.COMPANYCODE AND MRNREGISTER.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MRNREGISTER.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND MRNREGISTER.ITEMTYPECODE = ITEMTYPE.CODE` |
| `UNITOFMEASURE_UM` | `UMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `MRNREGISTER.UMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MRNREGISTERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.TAXCODE1,
       t.TAXCODE2,
       t.TAXCODE3,
       t.TAXCODE4,
       t.TAXCODE5,
       t.OTHERCODES,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.MRNREGISTER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
