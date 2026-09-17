# DB2ADMIN.REPLENISHMENTREQUISITIONEX

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `COMPANYCODE`, `REQUISITIONTEMPLATECODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 109871

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `REQUISITIONTEMPLATECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `CODE` | CHAR(15) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `RFQDETAILRFQHEADERCOUNTERCODE` | CHAR(8) |  | FK | foreign_key |  |
| 4 | `RFQDETAILRFQHEADERCODE` | CHAR(15) |  | FK | foreign_key |  |
| 5 | `RFQDETAILLINENO` | INTEGER |  | FK | foreign_key |  |
| 6 | `BUYERCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 7 | `BUYERCODE` | CHAR(25) |  | FK | foreign_key |  |
| 8 | `REMARK` | VARCHAR(200) |  |  |  |  |
| 9 | `ORDERPRIORITY` | CHAR(2) |  |  |  |  |
| 10 | `REQUESTREASON` | VARCHAR(200) |  |  |  |  |
| 11 | `SUGGESTEDSUPPLIER` | CHAR(100) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONEX.COMPANYCODE = COMPANY.CODE` |
| `INITIALS_BUYER` | `BUYERCOMPANYCODE`, `BUYERCODE` | [`INITIALS`](../CORE_MASTER/INITIALS.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONEX.BUYERCOMPANYCODE = INITIALS.COMPANYCODE AND REPLENISHMENTREQUISITIONEX.BUYERCODE = INITIALS.CODE` |
| `REQUISITIONTEMPLATE_REQUISITIONTEMPLATE` | `COMPANYCODE`, `REQUISITIONTEMPLATECODE` | [`REQUISITIONTEMPLATE`](../CORE_MASTER/REQUISITIONTEMPLATE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `REPLENISHMENTREQUISITIONEX.COMPANYCODE = REQUISITIONTEMPLATE.COMPANYCODE AND REPLENISHMENTREQUISITIONEX.REQUISITIONTEMPLATECODE = REQUISITIONTEMPLATE.CODE` |
| `RFQDETAIL_RFQDETAIL` | `COMPANYCODE`, `RFQDETAILRFQHEADERCOUNTERCODE`, `RFQDETAILRFQHEADERCODE`, `RFQDETAILLINENO` | [`RFQDETAIL`](../PURCHASING/RFQDETAIL.md) | `RFQHEADERCOMPANYCODE`, `RFQHEADERCOUNTERCODE`, `RFQHEADERCODE`, `LINENO` | RESTRICT | `REPLENISHMENTREQUISITIONEX.COMPANYCODE = RFQDETAIL.RFQHEADERCOMPANYCODE AND REPLENISHMENTREQUISITIONEX.RFQDETAILRFQHEADERCOUNTERCODE = RFQDETAIL.RFQHEADERCOUNTERCODE AND REPLENISHMENTREQUISITIONEX.RFQDETAILRFQHEADERCODE = RFQDETAIL.RFQHEADERCODE AND REPLENISHMENTREQUISITIONEX.RFQDETAILLINENO = RFQDETAIL.LINENO` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `REPLENISHMENTREQUISITIONEXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.REQUISITIONTEMPLATECODE,
       t.CODE,
       t.RFQDETAILRFQHEADERCOUNTERCODE,
       t.RFQDETAILRFQHEADERCODE,
       t.RFQDETAILLINENO,
       t.BUYERCOMPANYCODE,
       t.BUYERCODE,
       t.REMARK,
       t.ORDERPRIORITY,
       t.REQUESTREASON,
       t.SUGGESTEDSUPPLIER
FROM   DB2ADMIN.REPLENISHMENTREQUISITIONEX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
