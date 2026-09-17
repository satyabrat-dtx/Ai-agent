# DB2ADMIN.FMGSETTLEMENT

- **Module**: `HR` (low confidence — FK neighbourhood: 1 of 1 related tables are HR)
- **Roles**: `business_data`
- **Columns**: 20
- **Primary key**: `COMPANYCODE`, `FMGCODEFMGCODE`, `ASSETCODE`, `SERIALNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 156652

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `FMGCODEFMGCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ASSETCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 3 | `SERIALNUMBER` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 4 | `SETTLEMENTDATE` | DATE |  |  |  |  |
| 5 | `WDVAPPLICABLE` | INTEGER | NOT NULL |  |  |  |
| 6 | `DEPERICATIONPERCENTAGE` | DECIMAL(5,2) |  |  |  |  |
| 7 | `SELLBILLAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 8 | `PAIDAMOUNT` | DECIMAL(17,2) |  |  |  |  |
| 9 | `APPROVEDBYCODE` | CHAR(10) | NOT NULL |  |  |  |
| 10 | `APPROVEDDATE` | DATE |  |  |  |  |
| 11 | `PAYEMENTTRROUGH` | INTEGER | NOT NULL |  |  |  |
| 12 | `STATUS` | INTEGER | NOT NULL |  |  |  |
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
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `FMGSETTLEMENT.COMPANYCODE = COMPANY.CODE` |
| `FMGMASTER_FMGCODE` | `COMPANYCODE`, `FMGCODEFMGCODE` | [`FMGMASTER`](../HR/FMGMASTER.md) | `COMPANYCODE`, `FMGCODE` | RESTRICT | `FMGSETTLEMENT.COMPANYCODE = FMGMASTER.COMPANYCODE AND FMGSETTLEMENT.FMGCODEFMGCODE = FMGMASTER.FMGCODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FMGSETTLEMENTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.FMGCODEFMGCODE,
       t.ASSETCODE,
       t.SERIALNUMBER,
       t.SETTLEMENTDATE,
       t.WDVAPPLICABLE,
       t.DEPERICATIONPERCENTAGE,
       t.SELLBILLAMOUNT,
       t.PAIDAMOUNT,
       t.APPROVEDBYCODE,
       t.APPROVEDDATE,
       t.PAYEMENTTRROUGH
FROM   DB2ADMIN.FMGSETTLEMENT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
