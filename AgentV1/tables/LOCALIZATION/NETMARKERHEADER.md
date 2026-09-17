# DB2ADMIN.NETMARKERHEADER

- **Module**: `LOCALIZATION` (low confidence — table name starts with 'NET')
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `PRODUCTIONORDERCODE`, `RESERVATIONGROUPLINE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 217785

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PRODUCTIONORDERCODE` | CHAR(15) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RESERVATIONGROUPLINE` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 4 | `SHADEGRPUSGENGRPTECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `SHADEGRPUSGENGROUPTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `SHADEGROUPCODE` | CHAR(10) |  | FK | foreign_key |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `NETMARKERHEADER.COMPANYCODE = COMPANY.CODE` |
| `PRODUCTIONORDER_PRODUCTIONORDER` | `COMPANYCODE`, `PRODUCTIONORDERCODE` | [`PRODUCTIONORDER`](../PRODUCTION/PRODUCTIONORDER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `NETMARKERHEADER.COMPANYCODE = PRODUCTIONORDER.COMPANYCODE AND NETMARKERHEADER.PRODUCTIONORDERCODE = PRODUCTIONORDER.CODE` |
| `USERGENERICGROUP_SHADEGROUP` | `SHADEGRPUSGENGRPTECOMPANYCODE`, `SHADEGRPUSGENGROUPTYPECODE`, `SHADEGROUPCODE` | [`USERGENERICGROUP`](../CORE_MASTER/USERGENERICGROUP.md) | `USERGENGROUPTYPECOMPANYCODE`, `USERGENERICGROUPTYPECODE`, `CODE` | RESTRICT | `NETMARKERHEADER.SHADEGRPUSGENGRPTECOMPANYCODE = USERGENERICGROUP.USERGENGROUPTYPECOMPANYCODE AND NETMARKERHEADER.SHADEGRPUSGENGROUPTYPECODE = USERGENERICGROUP.USERGENERICGROUPTYPECODE AND NETMARKERHEADER.SHADEGROUPCODE = USERGENERICGROUP.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `NETMARKERHEADERUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PRODUCTIONORDERCODE,
       t.RESERVATIONGROUPLINE,
       t.CODE,
       t.SHADEGRPUSGENGRPTECOMPANYCODE,
       t.SHADEGRPUSGENGROUPTYPECODE,
       t.SHADEGROUPCODE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.NETMARKERHEADER t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
