# DB2ADMIN.VATPLAFONDDECLARATION

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 26
- **Primary key**: `COMPANYCODE`, `DIVISIONCODE`, `YEARSTRING`, `CODE`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 236209

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 2 | `YEARSTRING` | CHAR(4) | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | DECIMAL(5,0) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `DATEAPPLICATION` | DATE |  |  |  |  |
| 5 | `CUSTOMERSUPPLIERTYPE` | CHAR(1) |  | FK | foreign_key |  |
| 6 | `ORDPRNCUSTOMERSUPPLIERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 7 | `VATCODE` | CHAR(5) |  |  |  |  |
| 8 | `AMOUNT` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 9 | `DESCRIPTIONGOODS` | VARCHAR(140) |  |  |  |  |
| 10 | `NOTE` | VARCHAR(140) |  |  |  |  |
| 11 | `LIMITATIONUSAGE` | SMALLINT | NOT NULL |  |  |  |
| 12 | `LIMITDATEFROM` | DATE |  |  |  |  |
| 13 | `LIMITDATETO` | DATE |  |  |  |  |
| 14 | `APPROVAL` | SMALLINT | NOT NULL |  |  |  |
| 15 | `DATEAPPROVAL` | DATE |  |  |  |  |
| 16 | `TELEMATICOPROT` | DECIMAL(17,0) |  |  |  |  |
| 17 | `TELEMATICOSEQ` | CHAR(6) |  |  |  |  |
| 18 | `AMOUNTUSAGE` | DECIMAL(17,2) | NOT NULL |  |  |  |
| 19 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 20 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 21 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 22 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 25 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `VATPLAFONDDECLARATION.COMPANYCODE = COMPANY.CODE` |
| `ORDERPARTNER_ORDERPARTNER` | `COMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `ORDPRNCUSTOMERSUPPLIERCODE` | [`ORDERPARTNER`](../CORE_MASTER/ORDERPARTNER.md) | `CUSTOMERSUPPLIERCOMPANYCODE`, `CUSTOMERSUPPLIERTYPE`, `CUSTOMERSUPPLIERCODE` | RESTRICT | `VATPLAFONDDECLARATION.COMPANYCODE = ORDERPARTNER.CUSTOMERSUPPLIERCOMPANYCODE AND VATPLAFONDDECLARATION.CUSTOMERSUPPLIERTYPE = ORDERPARTNER.CUSTOMERSUPPLIERTYPE AND VATPLAFONDDECLARATION.ORDPRNCUSTOMERSUPPLIERCODE = ORDERPARTNER.CUSTOMERSUPPLIERCODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `VATPLAFONDDECLARATION_DECLARATIONUSAGE` | [`VATPLAFONDUSAGE`](../SALES/VATPLAFONDUSAGE.md) | `COMPANYCODE`, `DIVISIONCODE`, `YEARSTRING`, `CODE` | `VATPLAFONDUSAGE.COMPANYCODE = VATPLAFONDDECLARATION.COMPANYCODE AND VATPLAFONDUSAGE.DIVISIONCODE = VATPLAFONDDECLARATION.DIVISIONCODE AND VATPLAFONDUSAGE.YEARSTRING = VATPLAFONDDECLARATION.YEARSTRING AND VATPLAFONDUSAGE.CODE = VATPLAFONDDECLARATION.CODE` |

## Indexes

- `VATPLAFONDDECLARATIONUID` (ABSUNIQUEID)
- `VATPLADECL1` (COMPANYCODE, YEARSTRING, TELEMATICOPROT, TELEMATICOSEQ)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.YEARSTRING,
       t.CODE,
       t.DATEAPPLICATION,
       t.CUSTOMERSUPPLIERTYPE,
       t.ORDPRNCUSTOMERSUPPLIERCODE,
       t.VATCODE,
       t.AMOUNT,
       t.DESCRIPTIONGOODS,
       t.NOTE,
       t.LIMITATIONUSAGE
FROM   DB2ADMIN.VATPLAFONDDECLARATION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
