# DB2ADMIN.VAT

- **Module**: `FINANCE` (low confidence — FK neighbourhood: 3 of 3 related tables are FINANCE)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 7 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 103371

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 3 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 4 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 5 | `TAXTYPE` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `REPORTEUSALE` | CHAR(1) |  |  |  |  |
| 7 | `REPORTEUPURCHAS` | CHAR(1) |  |  |  |  |
| 8 | `ACTUALTAXATION` | SMALLINT | NOT NULL |  |  |  |
| 9 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `TOLERANCE` | DECIMAL(7,2) |  |  |  |  |
| 11 | `INITIALDATE` | DATE |  |  |  |  |
| 12 | `FINALDATE` | DATE |  |  |  |  |
| 13 | `INACTIVE` | SMALLINT | NOT NULL |  |  |  |
| 14 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 15 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 16 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 17 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `VAT.COMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `VAT.COUNTRYCODE = COUNTRY.CODE` |

## Referenced by (child → this table) — 7

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `VAT_TAXCODE` | [`FINVOULINES`](../FINANCE/FINVOULINES.md) | `FINVOUHEADERCOMPANYCODE`, `TAXCODECODE` | `FINVOULINES.FINVOUHEADERCOMPANYCODE = VAT.COMPANYCODE AND FINVOULINES.TAXCODECODE = VAT.CODE` |
| `VAT_TAXCODE` | [`FINVOUTAX`](../FINANCE/FINVOUTAX.md) | `FINVOUHEADERCOMPANYCODE`, `TAXCODECODE` | `FINVOUTAX.FINVOUHEADERCOMPANYCODE = VAT.COMPANYCODE AND FINVOUTAX.TAXCODECODE = VAT.CODE` |
| `VAT_TAX` | [`DEDUCTIONTYPE`](../FINANCE/DEDUCTIONTYPE.md) | `COMPANYCODE`, `TAXCODE` | `DEDUCTIONTYPE.COMPANYCODE = VAT.COMPANYCODE AND DEDUCTIONTYPE.TAXCODE = VAT.CODE` |
| `VAT_TAX` | [`FINVOUCHERTEMPLATE`](../FINANCE/FINVOUCHERTEMPLATE.md) | `COMPANYCODE`, `TAXCODE` | `FINVOUCHERTEMPLATE.COMPANYCODE = VAT.COMPANYCODE AND FINVOUCHERTEMPLATE.TAXCODE = VAT.CODE` |
| `VAT_TAXCODE` | [`GENERALLEDGERACCOUNT`](../FINANCE/GENERALLEDGERACCOUNT.md) | `COMPANYCODE`, `TAXCODECODE` | `GENERALLEDGERACCOUNT.COMPANYCODE = VAT.COMPANYCODE AND GENERALLEDGERACCOUNT.TAXCODECODE = VAT.CODE` |
| `VAT_TAXCODE` | [`TAXRETURNCOMPANY`](../FINANCE/TAXRETURNCOMPANY.md) | `COMPANYCODE`, `TAXCODECODE` | `TAXRETURNCOMPANY.COMPANYCODE = VAT.COMPANYCODE AND TAXRETURNCOMPANY.TAXCODECODE = VAT.CODE` |
| `VAT_VATDETAIL` | [`VATDETAIL`](../FINANCE/VATDETAIL.md) | `VATCOMPANYCODE`, `VATCODE` | `VATDETAIL.VATCOMPANYCODE = VAT.COMPANYCODE AND VATDETAIL.VATCODE = VAT.CODE` |

## Indexes

- `VATUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.TAXTYPE,
       t.REPORTEUSALE,
       t.REPORTEUPURCHAS,
       t.ACTUALTAXATION,
       t.COUNTRYCODE,
       t.TOLERANCE,
       t.INITIALDATE
FROM   DB2ADMIN.VAT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
