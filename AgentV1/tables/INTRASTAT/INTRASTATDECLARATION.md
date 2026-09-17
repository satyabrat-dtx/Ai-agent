# DB2ADMIN.INTRASTATDECLARATION

- **Module**: `INTRASTAT` (high confidence — table name starts with 'INTRASTAT')
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 216441

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 2 | `COUNTRYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 3 | `MULTICOUNTRY` | SMALLINT | NOT NULL |  |  |  |
| 4 | `DECLARATIONPOLICYCODE` | CHAR(20) |  |  |  |  |
| 5 | `FREQUENCY` | CHAR(1) | NOT NULL |  |  |  |
| 6 | `YEAR` | INTEGER | NOT NULL |  |  |  |
| 7 | `MONTH` | INTEGER | NOT NULL |  |  |  |
| 8 | `QUARTER` | INTEGER | NOT NULL |  |  |  |
| 9 | `PERIODICITY` | INTEGER | NOT NULL |  |  |  |
| 10 | `SALES` | SMALLINT | NOT NULL |  |  |  |
| 11 | `SALESFISCALPURPOSE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `SALESSTATISTICALPURPOSE` | SMALLINT | NOT NULL |  |  |  |
| 13 | `PURCHASES` | SMALLINT | NOT NULL |  |  |  |
| 14 | `PURCHASESSTATISTICALPURPOSE` | SMALLINT | NOT NULL |  |  |  |
| 15 | `PURCHASESFISCALPURPOSE` | SMALLINT | NOT NULL |  |  |  |
| 16 | `NOPREVIOUSDECLARATIONS` | SMALLINT | NOT NULL |  |  |  |
| 17 | `VATVARIATIONENDACTIVITIES` | SMALLINT | NOT NULL |  |  |  |
| 18 | `FILEPATH` | VARCHAR(250) | NOT NULL |  |  |  |
| 19 | `TAXREGISTRATIONNUMBER` | CHAR(15) | NOT NULL |  |  |  |
| 20 | `THIRDPARTYDECLARANT` | SMALLINT | NOT NULL |  |  |  |
| 21 | `THIRDPARTYTAXREGNUM` | CHAR(15) |  |  |  |  |
| 22 | `FILLNATUREB` | SMALLINT | NOT NULL |  |  |  |
| 23 | `CUSTOMCODE` | CHAR(6) |  |  |  |  |
| 24 | `SENT` | SMALLINT | NOT NULL |  |  |  |
| 25 | `SENTBYUSER` | CHAR(50) |  |  |  |  |
| 26 | `SENTDATE` | DATE |  |  |  |  |
| 27 | `RESTOREDSENTBYUSER` | CHAR(50) |  |  |  |  |
| 28 | `RESTOREDSENTDATE` | DATE |  |  |  |  |
| 29 | `PROTOCOL` | INTEGER | NOT NULL |  |  |  |
| 30 | `SALESREFERENCENUMBER` | INTEGER | NOT NULL |  |  |  |
| 31 | `PURCHASESREFERENCENUMBER` | INTEGER | NOT NULL |  |  |  |
| 32 | `FROMDATE` | DATE |  |  |  | Inclusive start of a validity period. |
| 33 | `TODATE` | DATE |  |  |  | End of a validity period. |
| 34 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 35 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 36 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 37 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 38 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 39 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `INTRASTATDECLARATION.COMPANYCODE = COMPANY.CODE` |
| `COUNTRY_COUNTRY` | `COUNTRYCODE` | [`COUNTRY`](../CORE_MASTER/COUNTRY.md) | `CODE` | RESTRICT | `INTRASTATDECLARATION.COUNTRYCODE = COUNTRY.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `INTRASTATDECLARATION_ROWS` | [`INTRASTATDECLARATIONROW`](../INTRASTAT/INTRASTATDECLARATIONROW.md) | `INTRASTATDECLARATIONCMYCODE`, `INTRASTATDECLARATIONCODE` | `INTRASTATDECLARATIONROW.INTRASTATDECLARATIONCMYCODE = INTRASTATDECLARATION.COMPANYCODE AND INTRASTATDECLARATIONROW.INTRASTATDECLARATIONCODE = INTRASTATDECLARATION.CODE` |

## Indexes

- `INTRASTATDECLARATIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CODE,
       t.COUNTRYCODE,
       t.MULTICOUNTRY,
       t.DECLARATIONPOLICYCODE,
       t.FREQUENCY,
       t.YEAR,
       t.MONTH,
       t.QUARTER,
       t.PERIODICITY,
       t.SALES,
       t.SALESFISCALPURPOSE
FROM   DB2ADMIN.INTRASTATDECLARATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
